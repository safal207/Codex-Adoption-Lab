# Proposed claim-matrix edits — 2026-10-19 (awaiting human verification)

**State: PROPOSED / HOLD, not approved, not an active matrix.** This is the complete copy-edit packet from the October 19 assistant [official-source inspection](12-source-review-2026-10-19.md). It is intentionally separated from the [active claim matrix](06-claim-evidence-matrix.md), which retains the earlier recorded wording and unchanged review dates, without implying independent human sign-off for the September historical-statistics rows.

**Approval contract:** On a per-claim basis, a human maintainer must open the relevant official page, compare its cited section with the proposed wording and the earlier statement, record any account/methodology limits, accept/revise/retire the claim, and only then update `Accessed` and `Review by` with the real human verification date according to the existing cadence. Do not backdate the review, extend a deadline to make CI green, infer the reviewer's approval from an assistant run, or turn the original HTTP 403 into a source-validity judgment.

## Exact proposed replacement text (copy only after verification)

| Claim ID | Proposed `Material claim` (not yet approved) | Proposed official evidence | Current Accessed → Review by (UNCHANGED, not proposed renewal) |
|---|---|---|---|
| C-001 | Codex is available across Free, Go, Plus, Pro, Business, Edu, and Enterprise, subject to plan eligibility. Free and Go show limited/trial Codex access, Plus expands usage, and Pro advertises intensive sessions and maximum tasks as a relative plan feature, not a guaranteed fixed task count. Rollout, model, surface, and account limits apply. | https://developers.openai.com/codex/pricing/ and https://chatgpt.com/codex/pricing/ | 2026-10-12 → 2026-10-19 |
| C-002 | Self-serve Business prices in USD per paid seat/month: Standard $20 billed annually or $25 monthly; Premium $100 billed annually or $125 monthly. At least two paid Standard/Premium seats in total are needed and they may be mixed; annual rates are monthly equivalents billed annually. Country/currency prices and included usage may differ. | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | 2026-10-12 → 2026-10-19 |
| C-010 | On June 2, 2026, OpenAI reported more than 5 million weekly active Codex users at that time; this dated report is not a live or October 2026 user count. | https://openai.com/index/codex-for-knowledge-work/ | 2026-09-17 → 2026-10-19 |
| C-011 | In its June 2, 2026 announcement, OpenAI described knowledge workers as about 20% of Codex users at that time, with that group growing more than three times as fast as developers. This is a dated, approximate comparison. | https://openai.com/index/codex-for-knowledge-work/ | 2026-09-17 → 2026-10-19 |
| C-012 | For May 2026, OpenAI reported that 70.2% of a random 0.1% sample of individual Codex users made at least one request with a human-task horizon estimated above one hour by LLM-as-judge using transcripts. This directional estimate measures neither actual work completed nor time saved. | https://openai.com/index/how-agents-are-transforming-work/ | 2026-09-17 → 2026-10-19 |
| C-014 | OpenAI describes Select, Advanced, and Elite Partner Network tier progression in terms of sales performance, technical capability, co-sell engagement, and deployment experience. Public enrollment asks applicants for company capabilities, technical expertise, and customer experience; industry expertise, relationships, and delivery capacity are emphasized. None proves Lab eligibility or affiliation. | https://openai.com/index/introducing-openai-partner-network/ and https://openai.com/business/partners/ | 2026-10-12 → 2026-10-26 |
| C-019 | Under applicable flexible credit-based Business/Enterprise/Edu billing, ChatGPT Work/Codex usage is priced in credits per 1M input, cached-input, and output tokens, with model/mode-specific rates. Eligible Business subscription usage draws from included limits before purchased credits; USD-billed Enterprise agreements and legacy arrangements may use different rate cards. These are not universal API or subscription prices. | https://help.openai.com/en/articles/11481834 | 2026-10-12 → 2026-10-19 |

The proposed wording keeps the existing classifications and freshness rules; the pending reviewer must decide whether the wording and evidence actually support each other before copying it into the active matrix. The observed 2026-10-19 assistant source-inspection date is **not** a substitute for `Accessed` under the repository's human-verification contract.

## Mandatory cross-checks

- [ ] **C-001** — Open the [current Codex pricing](https://chatgpt.com/codex/pricing/) and [ChatGPT/Codex pricing docs](https://developers.openai.com/codex/pricing/); distinguish Free/Go limited trial availability, Plus expanded usage, Pro comparison wording and actual account/rollout limits.
- [ ] **C-002** — Inspect the [current Business overview](https://help.openai.com/en/articles/8792828-chatgpt-business-overview): Standard/Premium annual-vs-monthly USD equivalents, two paid seats and mixing, distinct purchased vs assigned seats, geography, and API separation.
- [ ] **C-010** — Re-open the [June 2, 2026 Codex report](https://openai.com/index/codex-for-knowledge-work/) and ensure the 5 million figure remains labeled as **weekly** and dated, not current.
- [ ] **C-011** — Check the same June 2 article for approximate 20% knowledge-worker composition and **3x growth-rate comparison**, not an absolute result.
- [ ] **C-012** — Open [June 25 research and its footnotes](https://openai.com/index/how-agents-are-transforming-work/). Confirm May 2026, 70.2%, random 0.1% sample of individual users, an LLM-as-judge human-task-horizon estimate, and that no actual time saved or acceptance rate follows.
- [ ] **C-014** — Compare [Partner Network tiers](https://openai.com/index/introducing-openai-partner-network/) with [enrollment requirements](https://openai.com/business/partners/); no inference of Lab participation, partner endorsement or acceptance.
- [ ] **C-019** — Inspect [credit-based Work/Codex rate-card scope](https://help.openai.com/en/articles/11481834), with per-million-token dimensions, Standard mode, included seat limits, legacy seats, USD Enterprise agreements and exclusions.
- [ ] After human sign-off, update each row's `Accessed` and `Review by` with the true verification date and a separate attributed log entry. Leave unverified claims expired and unusable for external pricing/program claims.
- [ ] Run the trusted unit tests and documentation integrity at the real UTC date. Separately record HTTP reachability (`passed`/`blocked`/`transient`/`failed`); do not treat reachability or passing CI as semantic or human approval.

## Attribution and history

- 2026-09-17 and 2026-09-28: earlier source records remain intact.
- 2026-09-28: PR #12 merged, which is not independent source attestation.
- 2026-10-12: previous owner attestation covered **only** C-001/C-002/C-014/C-019 as worded in [the October 12 PR commit](https://github.com/safal207/Codex-Adoption-Lab/blob/334c8f062f35715d54f14bd0cf79a3c6b7c3d41e/docs/06-claim-evidence-matrix.md). C-010–C-012 still carry September 17 dates.
- 2026-10-19: assistant compared seven passages and drafted these alternative statements. **No fresh owner attestation was obtained.**
- The [October 19 scheduled failure](https://github.com/safal207/Codex-Adoption-Lab/actions/runs/39257120833) observed seven HTTP 403/BLOCKED responses; browser-based source inspection does not overwrite them.

**Release gate: HOLD until the checked source passages have actually been reviewed by the owner.**
