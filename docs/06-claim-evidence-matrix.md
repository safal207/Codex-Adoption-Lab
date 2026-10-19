# Claim–evidence matrix

**Latest source-content inspection:** 2026-10-19 (UTC), recorded as an [assistant-only review](12-source-review-2026-10-19.md) awaiting owner source verification. The [October 12 owner attestation](11-source-review-2026-10-12.md) covers the previously reviewed four claims only; it must not be read as approval of the new October 19 wording or of C-010–C-012. No verification dates were renewed by this pass.

**Approval status:** [PR #12](https://github.com/safal207/Codex-Adoption-Lab/pull/12) merged on 2026-09-28 at `71e80a170cb3cb494249108553dc1f383bbe5055`. Its [pre-merge review](https://github.com/safal207/Codex-Adoption-Lab/pull/12#pullrequestreview-5344750243) records merge authorization, explicitly not independent human source verification. For the October 12 inspection, Aleksey Safonov confirmed in the task conversation: “Да, проверил все четыре”, responding to the explicit question about personally opening the sources and confirming the four scoped claims. This is a recorded owner attestation, not a GitHub APPROVED review or retroactive verification of PR #12.

**Purpose:** map each material public claim to a specific official source, classification, and machine-checkable review date.

This file is part of the evidence contract. A source list at the end of a document is not sufficient when a reader cannot determine which source supports which claim.

## Classifications

- `official fact` — stated by OpenAI in an official product, help, pricing, or announcement page.
- `official fact with methodology limitation` — official data that must retain sampling, estimation, date, or methodology qualifiers.
- `official fact / documentation rule` — official status plus a rule for representing it accurately.
- `Lab hypothesis` — reasoned hypothesis requiring measurement.
- `Lab inference` — internal interpretation based on available evidence.
- `Lab proposal` — proposed strategy, experiment, metric, or commercial term.

## Active matrix

`Review by` uses ISO `YYYY-MM-DD`. For non-official claims, use `n/a`. The integrity checker fails when an official claim is past its review date.

**Source-verification boundary:** the October 19 observations below are proposed refinements pending maintainer review. An assistant page read, green CI, or HTTP success does not reset `Accessed` / `Review by`; the existing recorded dates deliberately remain unchanged.

| Claim ID | Material claim | Classification | Official evidence | Published / updated | Accessed | Review by | Freshness rule |
|---|---|---|---|---|---|---|---|
| C-001 | Codex is available across Free, Go, Plus, Pro, Business, Edu, and Enterprise, subject to plan eligibility. Free and Go show limited/trial Codex access, Plus expands usage, and Pro advertises intensive sessions and maximum tasks as a relative plan feature, not a guaranteed fixed task count. Rollout, model, surface, and account limits apply. | official fact | https://developers.openai.com/codex/pricing/ and https://chatgpt.com/codex/pricing/ | live pricing documentation | 2026-10-12 | 2026-10-19 | Recheck before every external use and at least weekly during a launch. |
| C-002 | Self-serve Business prices in USD per paid seat/month: Standard $20 billed annually or $25 monthly; Premium $100 billed annually or $125 monthly. At least two paid Standard/Premium seats in total are needed and they may be mixed; annual rates are monthly equivalents billed annually. Country/currency prices and included usage may differ. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | live help article (redirects to current Business overview) | 2026-10-12 | 2026-10-19 | Recheck before every external use and at least weekly during a launch. |
| C-003 | Standard and Premium Business seats include ChatGPT, Work, and Codex; API usage is billed separately. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | live help article | 2026-09-28 | 2026-10-28 | Recheck monthly and before a proposal. |
| C-004 | Legacy Business Codex-only seats remain limited to eligible workspaces that added that seat type before June 24, 2026. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | live help article | 2026-09-28 | 2026-10-28 | Recheck monthly and before any seat recommendation. |
| C-010 | On June 2, 2026, OpenAI reported more than 5 million weekly active Codex users at that time; this dated report is not a live or October 2026 user count. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-09-17 | 2026-10-19 | Keep the publication date; do not present as a current count. |
| C-011 | In its June 2, 2026 announcement, OpenAI described knowledge workers as about 20% of Codex users at that time, with that group growing more than three times as fast as developers. This is a dated, approximate comparison. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-09-17 | 2026-10-19 | Preserve historical framing and approximation. |
| C-012 | For May 2026, OpenAI reported that 70.2% of a random 0.1% sample of individual Codex users made at least one request with a human-task horizon estimated above one hour by LLM-as-judge using transcripts. This directional estimate measures neither actual work completed nor time saved. | official fact with methodology limitation | https://openai.com/index/how-agents-are-transforming-work/ | 2026-06-25 | 2026-09-17 | 2026-10-19 | Preserve sample, model-estimated duration, and measurement month; do not infer Lab results. |
| C-013 | OpenAI launched the Partner Network to support workflow adoption and implementation. | official fact | https://openai.com/index/introducing-openai-partner-network/ | 2026-06-14 | 2026-09-28 | 2026-10-28 | Recheck monthly and before partner outreach. |
| C-014 | OpenAI describes Select, Advanced, and Elite Partner Network tier progression in terms of sales performance, technical capability, co-sell engagement, and deployment experience. Public enrollment asks applicants for company capabilities, technical expertise, and customer experience; industry expertise, relationships, and delivery capacity are emphasized. None proves Lab eligibility or affiliation. | official fact | https://openai.com/index/introducing-openai-partner-network/ and https://openai.com/business/partners/ | live / 2026-06-14 | 2026-10-12 | 2026-10-26 | Recheck at least fortnightly and before enrollment or qualification claims. |
| C-015 | Helping a user complete one accepted workflow before recommending a plan may improve activation and plan confidence. | Lab hypothesis | Supported directionally by C-013; requires experiment | n/a | 2026-07-21 | n/a | Never state as proven until measured. |
| C-016 | The QA/Product segment is an attractive initial wedge because its work is evidence-heavy, reviewable, and repeatable. | Lab inference | Internal workflow analysis; not an OpenAI claim | n/a | 2026-07-21 | n/a | Validate through interviews and seed cases. |
| C-017 | A seven-day Build Week and three-event education sequence can improve activation, retention, or conversion. | Lab proposal | `docs/02-plf-launch-strategy.md` | n/a | 2026-07-21 | n/a | Requires controlled measurement; do not claim causality in advance. |
| C-018 | A 5–10% revenue share could be a negotiation option. | Lab proposal | `docs/04-partnership-proposal.md` | n/a | 2026-07-21 | n/a | Not an OpenAI term or market standard; use only after attribution and procurement review. |
| C-019 | Under applicable flexible credit-based Business/Enterprise/Edu billing, ChatGPT Work/Codex usage is priced in credits per 1M input, cached-input, and output tokens, with model/mode-specific rates. Eligible Business subscription usage draws from included limits before purchased credits; USD-billed Enterprise agreements and legacy arrangements may use different rate cards. These are not universal API or subscription prices. | official fact | https://help.openai.com/en/articles/11481834 | live credit-based rate card (redirects to current article) | 2026-10-12 | 2026-10-19 | Recheck weekly and before a budget recommendation. |
| C-020 | A subset of Enterprise customers still uses legacy Codex rates until migration; the agreement determines applicable billing. | official fact | https://help.openai.com/en/articles/11481834 | live help article | 2026-09-28 | 2026-10-28 | Recheck monthly and against the participant's agreement. |

## Retired claim IDs

`C-005` through `C-009` are withdrawn from current guidance as of 2026-09-17. They are not reclassified as hypotheses or silently assigned new expiry dates. Their original wording, access dates, and expired deadlines remain in the [pre-review matrix](https://github.com/safal207/Codex-Adoption-Lab/blob/98a9c273458f6550207e4536648deedfb16c3ff9/docs/06-claim-evidence-matrix.md).

| Retired ID | Disposition |
|---|---|
| C-005 | April transition summary is not supported by the redirected source now; current billing scope is recorded separately in C-019. |
| C-006 | Universal migration wording is unsuitable for current guidance; the current source retains a legacy Enterprise exception (C-020). |
| C-007 | July model prices are superseded by later price-change notices. The static table is removed. |
| C-008 | Cache details are retired with the model-specific cost table; this is a scope reduction, not a claim that the old cache rule is false. |
| C-009 | Preview-based availability guidance is removed. Check live account/model access for each run. |

See the [September 17 source-review record](09-source-review-2026-09-17.md) for the retirement decisions and the [September 28 review](10-source-review-2026-09-28.md) for earlier active-source checks; see the [October 12 record](11-source-review-2026-10-12.md) for the four renewed claims. The [October 19 inspection](12-source-review-2026-10-19.md) adds proposed corrections without renewing any dates. Retired IDs must not support new external claims. This pass does not validate the five retired statements.

## Rules for downstream documents

1. Reference the claim ID next to each material external claim where practical.
2. Preserve qualifiers such as `estimated`, `sampled`, `preview`, `about`, and exact dates.
3. Never convert a Lab inference into an official fact.
4. When a live pricing or help page changes, update this matrix before updating derived documents.
5. Record old values in version history rather than silently rewriting historical evidence.
6. External one-pagers should include only claims whose freshness check passed within the required window.
7. Update both `Accessed` and `Review by` after a human verifies the source.
8. Record assistant-only source inspections separately without changing claim freshness or converting `BLOCKED` HTTP access into proof of source validity.

## Review log

| Version | Date | Reviewer | Change |
|---|---|---|---|
| 0.1 | 2026-07-21 | CAL-001 facilitator review | Initial material-claim mapping and freshness rules |
| 0.2 | 2026-07-21 | Documentation-integrity implementation | Added machine-checkable review dates |
| 0.3 | 2026-09-17 | Codex-assisted source review; proposed for maintainer approval in the pull request | Rechecked active sources, corrected Business seats, withdrew C-005–C-009, added C-019/C-020, and dated historical statistics; checker rules unchanged |
| 0.4 | 2026-09-28 | Assistant-assisted source review; pending at review time in PR #12 (merged September 28; independent human source verification not recorded) | Rechecked C-001–C-004, C-013/C-014, C-019/C-020; clarified C-019 scope; left C-010–C-012 dates and all retirement decisions unchanged |
| 0.5 | 2026-10-12 | Assistant source inspection; human source verification pending | Proposed corrections for C-001/C-002/C-014/C-019; recorded live sources and limitations; corrected merged PR #12 status; no freshness dates extended |
| 0.6 | 2026-10-12 | Aleksey Safonov; personal source-verification attestation in task conversation | Confirmed C-001/C-002/C-019/C-014; applied verified wording and renewed only their dates under existing weekly/fortnightly rules; no GitHub review or merge approval inferred |
| 0.7 | 2026-10-19 | ChatGPT assistant; source inspection only, fresh owner verification pending | Compared C-001/C-002/C-014/C-019 and C-010–C-012 with current official pages; refined scoped wording and C-012 methodology; kept all `Accessed` and `Review by` dates, older review records, retired IDs and CI gate unchanged |
