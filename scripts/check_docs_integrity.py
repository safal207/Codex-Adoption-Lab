#!/usr/bin/env python3
"""Check documentation links, claim freshness, and external-material guardrails.

The checker uses only Python's standard library. It treats repository content as
untrusted data: it never imports or executes files from the target tree.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Iterable

MAX_FILE_BYTES = 5 * 1024 * 1024
MAX_TOTAL_BYTES = 25 * 1024 * 1024
DEFAULT_OFFICIAL_DOMAINS = {
    "openai.com",
    "www.openai.com",
    "chatgpt.com",
    "www.chatgpt.com",
    "help.openai.com",
    "developers.openai.com",
}

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
BARE_URL_RE = re.compile(r"https?://[^\s<>|)]+")
FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
CLAIM_ID_RE = re.compile(r"^C-\d{3}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

PROHIBITED_EXTERNAL_PATTERNS = {
    "unapproved partner claim": re.compile(
        r"\b(?:official|certified|authorized)\s+OpenAI\s+partner\b", re.IGNORECASE
    ),
    "guaranteed outcome": re.compile(
        r"\bguaranteed\s+(?:savings|income|revenue|conversion|ROI)\b", re.IGNORECASE
    ),
    "synthetic proof claim": re.compile(
        r"\bsynthetic\s+(?:example|case|data).{0,80}\b(?:proves?|demonstrates?|validates?)\b",
        re.IGNORECASE,
    ),
}


@dataclasses.dataclass(frozen=True)
class Finding:
    check: str
    status: str
    path: str
    message: str
    line: int | None = None
    target: str | None = None

    def as_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Target repository tree")
    parser.add_argument(
        "--as-of",
        type=str,
        default=dt.date.today().isoformat(),
        help="Date used for freshness checks (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--matrix",
        type=Path,
        default=Path("docs/06-claim-evidence-matrix.md"),
        help="Claim-evidence matrix path relative to root",
    )
    parser.add_argument("--report", type=Path, default=Path("docs-integrity-report.json"))
    parser.add_argument("--check-external", action="store_true")
    parser.add_argument(
        "--official-domain",
        action="append",
        dest="official_domains",
        help="External domain to check; repeatable. Defaults to official OpenAI domains.",
    )
    parser.add_argument("--timeout", type=float, default=12.0)
    return parser.parse_args()


def safe_read(path: Path, total: list[int]) -> str:
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        raise ValueError(f"file exceeds {MAX_FILE_BYTES} bytes")
    total[0] += size
    if total[0] > MAX_TOTAL_BYTES:
        raise ValueError(f"documentation exceeds {MAX_TOTAL_BYTES} bytes")
    return path.read_text(encoding="utf-8")


def markdown_files(root: Path) -> list[Path]:
    excluded = {".git", ".venv", "venv", "node_modules", "dist", "build"}
    result: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in excluded for part in path.parts):
            continue
        if path.is_file():
            result.append(path)
    return sorted(result)


def strip_fenced_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def normalize_link_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    # Optional Markdown title: path "title" or path 'title'.
    match = re.match(r"^(\S+)(?:\s+[\"'].*[\"'])?$", raw)
    return match.group(1) if match else raw


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def resolve_internal_target(source: Path, target: str, root: Path) -> Path | None:
    parsed = urllib.parse.urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith("//"):
        return None
    if target.startswith("#") or target.startswith("mailto:") or target.startswith("tel:"):
        return None

    decoded = urllib.parse.unquote(parsed.path)
    if not decoded:
        return None

    candidate = (root / decoded.lstrip("/")) if decoded.startswith("/") else (source.parent / decoded)
    candidate = candidate.resolve()
    root_resolved = root.resolve()
    try:
        candidate.relative_to(root_resolved)
    except ValueError:
        return candidate

    if candidate.is_dir():
        candidate = candidate / "README.md"
    return candidate


def check_internal_links(root: Path, files: Iterable[Path], texts: dict[Path, str]) -> list[Finding]:
    findings: list[Finding] = []
    root_resolved = root.resolve()
    for source in files:
        text = strip_fenced_code(texts[source])
        for match in MARKDOWN_LINK_RE.finditer(text):
            raw_target = normalize_link_target(match.group(1))
            if raw_target.startswith(("http://", "https://")):
                continue
            candidate = resolve_internal_target(source, raw_target, root)
            if candidate is None:
                continue
            try:
                candidate.relative_to(root_resolved)
            except ValueError:
                findings.append(
                    Finding(
                        "internal-link",
                        "failed",
                        str(source.relative_to(root)),
                        "link escapes repository root",
                        line_number(text, match.start()),
                        raw_target,
                    )
                )
                continue
            if not candidate.exists():
                findings.append(
                    Finding(
                        "internal-link",
                        "failed",
                        str(source.relative_to(root)),
                        "target does not exist",
                        line_number(text, match.start()),
                        raw_target,
                    )
                )
    if not findings:
        findings.append(Finding("internal-link", "passed", ".", "all internal Markdown links resolve"))
    return findings


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_matrix(matrix_path: Path, text: str) -> tuple[list[dict[str, str]], list[Finding]]:
    findings: list[Finding] = []
    lines = text.splitlines()
    header_index: int | None = None
    headers: list[str] = []
    for index, line in enumerate(lines):
        if line.lstrip().startswith("| Claim ID |"):
            header_index = index
            headers = split_table_row(line)
            break
    if header_index is None or header_index + 2 >= len(lines):
        return [], [Finding("claim-matrix", "failed", str(matrix_path), "matrix table not found")]

    required = {"Claim ID", "Classification", "Official evidence", "Accessed", "Review by"}
    missing = required.difference(headers)
    if missing:
        return [], [
            Finding(
                "claim-matrix",
                "failed",
                str(matrix_path),
                f"missing required columns: {', '.join(sorted(missing))}",
            )
        ]

    rows: list[dict[str, str]] = []
    for index in range(header_index + 2, len(lines)):
        line = lines[index]
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = split_table_row(line)
        if len(cells) != len(headers):
            findings.append(
                Finding(
                    "claim-matrix",
                    "failed",
                    str(matrix_path),
                    f"row has {len(cells)} cells; expected {len(headers)}",
                    index + 1,
                )
            )
            continue
        row = dict(zip(headers, cells, strict=True))
        if not CLAIM_ID_RE.match(row["Claim ID"]):
            findings.append(
                Finding("claim-matrix", "failed", str(matrix_path), "invalid claim ID", index + 1)
            )
        rows.append(row)

    ids = [row["Claim ID"] for row in rows]
    duplicates = sorted({claim_id for claim_id in ids if ids.count(claim_id) > 1})
    if duplicates:
        findings.append(
            Finding("claim-matrix", "failed", str(matrix_path), f"duplicate claim IDs: {duplicates}")
        )
    if not rows:
        findings.append(Finding("claim-matrix", "failed", str(matrix_path), "matrix has no claim rows"))
    return rows, findings


def check_freshness(root: Path, matrix_relative: Path, as_of: dt.date, total: list[int]) -> tuple[list[Finding], list[str]]:
    matrix_path = root / matrix_relative
    if not matrix_path.exists():
        return [Finding("claim-freshness", "failed", str(matrix_relative), "matrix file missing")], []
    text = safe_read(matrix_path, total)
    rows, findings = parse_matrix(matrix_relative, text)
    external_urls: list[str] = []

    for row in rows:
        claim_id = row["Claim ID"]
        classification = row["Classification"].lower()
        evidence = row["Official evidence"]
        external_urls.extend(BARE_URL_RE.findall(evidence))

        accessed = row["Accessed"]
        review_by = row["Review by"]
        if "official fact" in classification:
            if not DATE_RE.match(accessed):
                findings.append(
                    Finding("claim-freshness", "failed", str(matrix_relative), f"{claim_id}: invalid Accessed date")
                )
            if not DATE_RE.match(review_by):
                findings.append(
                    Finding("claim-freshness", "failed", str(matrix_relative), f"{claim_id}: invalid Review by date")
                )
                continue
            deadline = dt.date.fromisoformat(review_by)
            if as_of > deadline:
                findings.append(
                    Finding(
                        "claim-freshness",
                        "failed",
                        str(matrix_relative),
                        f"{claim_id}: claim expired on {deadline.isoformat()}",
                    )
                )
            else:
                findings.append(
                    Finding(
                        "claim-freshness",
                        "passed",
                        str(matrix_relative),
                        f"{claim_id}: current through {deadline.isoformat()}",
                    )
                )
    return findings, sorted(set(url.rstrip(".,;" ) for url in external_urls))


def external_paths(root: Path) -> list[Path]:
    prefixes = ("external", "outreach", "partner-facing")
    result: list[Path] = []
    for prefix in prefixes:
        base = root / prefix
        if base.exists():
            result.extend(path for path in base.rglob("*.md") if path.is_file())
    return sorted(set(result))


def check_external_material_guardrails(root: Path, total: list[int]) -> list[Finding]:
    findings: list[Finding] = []
    paths = external_paths(root)
    for path in paths:
        text = safe_read(path, total)
        for name, pattern in PROHIBITED_EXTERNAL_PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append(
                    Finding(
                        "external-guardrail",
                        "failed",
                        str(path.relative_to(root)),
                        name,
                        line_number(text, match.start()),
                    )
                )
    if not findings:
        message = "no prohibited patterns found" if paths else "no external-material directory present"
        findings.append(Finding("external-guardrail", "passed", ".", message))
    return findings


def request_url(url: str, timeout: float) -> tuple[str, str]:
    headers = {"User-Agent": "Codex-Adoption-Lab-docs-integrity/1.0"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = response.status
                if 200 <= status < 400:
                    return "passed", f"HTTP {status}"
                return "failed", f"HTTP {status}"
        except urllib.error.HTTPError as error:
            if error.code == 405 and method == "HEAD":
                continue
            if error.code in {401, 403}:
                return "blocked", f"HTTP {error.code}"
            if error.code == 429 or error.code >= 500:
                return "transient", f"HTTP {error.code}"
            return "failed", f"HTTP {error.code}"
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            return "transient", type(error).__name__
    return "failed", "no response"


def check_external_urls(urls: Iterable[str], domains: set[str], timeout: float) -> list[Finding]:
    findings: list[Finding] = []
    for url in sorted(set(urls)):
        host = (urllib.parse.urlsplit(url).hostname or "").lower()
        if host not in domains:
            findings.append(Finding("external-link", "skipped", ".", "domain not allowlisted", target=url))
            continue
        status, message = request_url(url, timeout)
        findings.append(Finding("external-link", status, ".", message, target=url))
    if not findings:
        findings.append(Finding("external-link", "skipped", ".", "no official external URLs found"))
    return findings


def summarize(findings: Iterable[Finding]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.status] = counts.get(finding.status, 0) + 1
    return dict(sorted(counts.items()))


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    try:
        as_of = dt.date.fromisoformat(args.as_of)
    except ValueError:
        print("--as-of must use YYYY-MM-DD", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"root does not exist: {root}", file=sys.stderr)
        return 2

    total = [0]
    findings: list[Finding] = []
    try:
        files = markdown_files(root)
        texts = {path: safe_read(path, total) for path in files}
        findings.extend(check_internal_links(root, files, texts))
        freshness, matrix_urls = check_freshness(root, args.matrix, as_of, total)
        findings.extend(freshness)
        findings.extend(check_external_material_guardrails(root, total))
        if args.check_external:
            domains = set(args.official_domains or DEFAULT_OFFICIAL_DOMAINS)
            findings.extend(check_external_urls(matrix_urls, domains, args.timeout))
    except (OSError, UnicodeError, ValueError) as error:
        findings.append(Finding("checker", "failed", ".", str(error)))

    report = {
        "schema_version": 1,
        "checker_version": "1.0.0",
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "as_of": as_of.isoformat(),
        "root": str(root),
        "external_checked": bool(args.check_external),
        "summary": summarize(findings),
        "findings": [finding.as_dict() for finding in findings],
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for finding in findings:
        location = finding.path + (f":{finding.line}" if finding.line else "")
        target = f" [{finding.target}]" if finding.target else ""
        print(f"{finding.status.upper():9} {finding.check:20} {location}: {finding.message}{target}")

    blocking = [finding for finding in findings if finding.status == "failed"]
    print(json.dumps({"summary": report["summary"], "report": str(args.report)}))
    return 1 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
