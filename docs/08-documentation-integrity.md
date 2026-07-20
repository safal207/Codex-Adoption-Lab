# Documentation integrity controls

The repository depends on volatile product, pricing, availability, and partner-program information. These controls prevent a stale or broken evidence package from being treated as current.

## What is checked

### On pull requests and pushes to `main`

- internal Markdown links;
- claim-matrix structure;
- unique claim IDs;
- ISO `Accessed` and `Review by` dates for official claims;
- expired official claims;
- prohibited language in files placed under `external/`, `outreach/`, or `partner-facing/`.

### On the weekly schedule and manual runs

The same checks run, plus reachability checks for official URLs found in the claim-evidence matrix.

External responses are classified as:

- `passed` — HTTP 2xx or 3xx;
- `failed` — confirmed client error such as 404 or 410;
- `blocked` — access denied, commonly 401 or 403;
- `transient` — timeout, rate limit, network failure, or server error;
- `skipped` — the domain is not on the official-source allowlist.

Only `failed` results block the checker. `blocked` and `transient` results remain visible for human review.

## Security model

The pull-request workflow uses `pull_request_target`, but it does **not** execute code from the pull request.

```text
Default branch
    ↓
trusted checker code

Pull request head
    ↓
checked out separately as untrusted data
    ↓
Markdown is parsed, never imported or executed
```

Additional controls:

- `contents: read` only;
- no secrets;
- pinned action commit SHAs;
- credentials are not persisted in either checkout;
- bounded file and total documentation sizes;
- no shell execution from the target tree;
- ten-minute job timeout.

## Claim freshness contract

`docs/06-claim-evidence-matrix.md` contains one row per material claim.

For every classification containing `official fact`, the checker requires:

- a valid claim ID such as `C-001`;
- an ISO `Accessed` date;
- an ISO `Review by` date;
- at least one evidence field.

A claim fails after its `Review by` date. A human must then:

1. open the official source;
2. confirm, revise, or retire the claim;
3. preserve required qualifiers;
4. update `Accessed`;
5. set a new `Review by` date;
6. record the change in the review log.

Do not extend a review date without checking the source.

## Local or manual fallback

From the repository root:

```bash
python3 scripts/check_docs_integrity.py \
  --root . \
  --as-of "$(date -u +%F)" \
  --report docs-integrity-report.json
```

To include official external URL checks:

```bash
python3 scripts/check_docs_integrity.py \
  --root . \
  --as-of "$(date -u +%F)" \
  --check-external \
  --report docs-integrity-report.json
```

The checker uses only the Python standard library and returns:

- exit code `0` when no blocking failure exists;
- exit code `1` for broken internal links, invalid or expired claims, prohibited external language, or confirmed broken official URLs;
- exit code `2` for invalid checker invocation.

## Report

Each run writes a JSON report containing:

- checker and schema versions;
- generation time and `as-of` date;
- whether external checks ran;
- counts by result class;
- every finding with check, path, line, message, and target where applicable.

GitHub Actions uploads this report for 30 days and writes a compact summary to the run page.

## External-material guardrails

Files intended for direct external use should live under one of:

- `external/`;
- `outreach/`;
- `partner-facing/`.

The checker currently blocks:

- unapproved claims of being an official, certified, or authorized OpenAI partner;
- guaranteed savings, income, revenue, conversion, or ROI;
- language presenting a synthetic example as proof or validation.

This is a minimum automated guardrail, not a replacement for human legal, brand, privacy, or factual review.

## Versioning

- Checker version: `1.0.0`
- Report schema: `1`
- Workflow actions: pinned by immutable commit SHA
- Initial implementation: issue #6, following CAL-001 finding `CAL-001-06`
