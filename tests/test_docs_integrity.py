from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_docs_integrity.py"
SPEC = importlib.util.spec_from_file_location("docs_integrity", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DocumentationIntegrityTests(unittest.TestCase):
    def write(self, root: Path, relative: str, content: str) -> Path:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def matrix(self, review_by: str = "2026-07-28") -> str:
        return f"""# Matrix

| Claim ID | Material claim | Classification | Official evidence | Published / updated | Accessed | Review by | Freshness rule |
|---|---|---|---|---|---|---|---|
| C-001 | Current price. | official fact | https://openai.com/example/ | live | 2026-07-21 | {review_by} | Recheck weekly. |
| C-002 | Proposed experiment. | Lab proposal | internal | n/a | 2026-07-21 | n/a | Measure before claiming. |
"""

    def test_valid_internal_link_and_current_claim_pass(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = self.write(root, "README.md", "[Audit](docs/audit.md)\n")
            target = self.write(root, "docs/audit.md", "# Audit\n")
            matrix = self.write(root, "docs/06-claim-evidence-matrix.md", self.matrix())
            texts = {path: path.read_text(encoding="utf-8") for path in (source, target, matrix)}

            link_findings = MODULE.check_internal_links(root, texts.keys(), texts)
            freshness, _ = MODULE.check_freshness(
                root, Path("docs/06-claim-evidence-matrix.md"), date(2026, 7, 21), [0]
            )

            self.assertFalse(any(item.status == "failed" for item in link_findings))
            self.assertFalse(any(item.status == "failed" for item in freshness))

    def test_broken_internal_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = self.write(root, "README.md", "[Missing](docs/missing.md)\n")
            texts = {source: source.read_text(encoding="utf-8")}

            findings = MODULE.check_internal_links(root, texts.keys(), texts)

            self.assertTrue(any(item.status == "failed" for item in findings))

    def test_expired_official_claim_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(
                root,
                "docs/06-claim-evidence-matrix.md",
                self.matrix(review_by="2026-07-20"),
            )

            findings, _ = MODULE.check_freshness(
                root, Path("docs/06-claim-evidence-matrix.md"), date(2026, 7, 21), [0]
            )

            self.assertTrue(any("expired" in item.message for item in findings))

    def test_external_partner_claim_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "external/one-pager.md", "We are an official OpenAI partner.\n")

            findings = MODULE.check_external_material_guardrails(root, [0])

            self.assertTrue(any(item.status == "failed" for item in findings))


if __name__ == "__main__":
    unittest.main()
