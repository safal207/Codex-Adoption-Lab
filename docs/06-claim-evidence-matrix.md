# Claim–evidence matrix

**Source review date:** 2026-09-17

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

| Claim ID | Material claim | Classification | Official evidence | Published / updated | Accessed | Review by | Freshness rule |
|---|---|---|---|---|---|---|---|
| C-001 | Free and Go offer limited Codex access; Plus expands usage; Pro lists maximum Codex tasks, subject to limits. | official fact | https://chatgpt.com/pricing/ | live pricing page | 2026-09-17 | 2026-09-24 | Recheck before every external use and at least weekly during a launch. |
| C-002 | Business prices in USD per user/month: Standard $20 billed annually or $25 monthly; Premium $100 billed annually or $125 monthly. Two Standard/Premium seats in total are required; regional prices may differ. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | live help article | 2026-09-17 | 2026-09-24 | Recheck before every external use and at least weekly during a launch. |
| C-003 | Standard and Premium Business seats include ChatGPT, Work, and Codex; API usage is billed separately. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | live help article | 2026-09-17 | 2026-10-17 | Recheck monthly and before a proposal. |
| C-004 | Legacy Business Codex-only seats remain limited to eligible workspaces that added that seat type before June 24, 2026. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | live help article | 2026-09-17 | 2026-10-17 | Recheck monthly and before any seat recommendation. |
| C-010 | On June 2, 2026, OpenAI reported more than 5 million weekly Codex users; this is historical, not a September count. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-09-17 | 2026-10-19 | Keep the publication date; do not present as a current count. |
| C-011 | The June 2 report put knowledge workers at about 20% of users, growing over three times as fast as developers. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-09-17 | 2026-10-19 | Preserve historical framing and approximation. |
| C-012 | In May 2026, 70.2% of sampled individual users requested at least one task estimated to exceed one hour of human work; this does not measure savings. | official fact with methodology limitation | https://openai.com/index/how-agents-are-transforming-work/ | 2026-06-25 | 2026-09-17 | 2026-10-19 | Preserve sample, model-estimated duration, and measurement month; do not infer Lab results. |
| C-013 | OpenAI launched the Partner Network to support workflow adoption and implementation. | official fact | https://openai.com/index/introducing-openai-partner-network/ | 2026-06-14 | 2026-09-17 | 2026-10-17 | Recheck monthly and before partner outreach. |
| C-014 | Partner Network materials emphasize sales, technical and deployment capability, co-selling, industry experience, delivery capacity, and customer relationships. | official fact | https://openai.com/index/introducing-openai-partner-network/ and https://openai.com/business/partners/ | live / 2026-06-14 | 2026-09-17 | 2026-10-01 | Recheck before enrollment or qualification claims. |
| C-015 | Helping a user complete one accepted workflow before recommending a plan may improve activation and plan confidence. | Lab hypothesis | Supported directionally by C-013; requires experiment | n/a | 2026-07-21 | n/a | Never state as proven until measured. |
| C-016 | The QA/Product segment is an attractive initial wedge because its work is evidence-heavy, reviewable, and repeatable. | Lab inference | Internal workflow analysis; not an OpenAI claim | n/a | 2026-07-21 | n/a | Validate through interviews and seed cases. |
| C-017 | A seven-day Build Week and three-event education sequence can improve activation, retention, or conversion. | Lab proposal | `docs/02-plf-launch-strategy.md` | n/a | 2026-07-21 | n/a | Requires controlled measurement; do not claim causality in advance. |
| C-018 | A 5–10% revenue share could be a negotiation option. | Lab proposal | `docs/04-partnership-proposal.md` | n/a | 2026-07-21 | n/a | Not an OpenAI term or market standard; use only after attribution and procurement review. |
| C-019 | The credit-based ChatGPT rate card meters Work and Codex by input, cached-input, and output tokens. | official fact | https://help.openai.com/en/articles/11481834 | live help article | 2026-09-17 | 2026-09-24 | Recheck weekly and before a budget recommendation. |
| C-020 | A subset of Enterprise customers still uses legacy Codex rates until migration; the agreement determines applicable billing. | official fact | https://help.openai.com/en/articles/11481834 | live help article | 2026-09-17 | 2026-10-17 | Recheck monthly and against the participant's agreement. |

## Retired claim IDs

`C-005` through `C-009` are withdrawn from current guidance as of 2026-09-17. They are not reclassified as hypotheses or silently assigned new expiry dates. Their original wording, access dates, and expired deadlines remain in the [pre-review matrix](https://github.com/safal207/Codex-Adoption-Lab/blob/98a9c273458f6550207e4536648deedfb16c3ff9/docs/06-claim-evidence-matrix.md).

| Retired ID | Disposition |
|---|---|
| C-005 | April transition summary is not supported by the redirected source now; current billing scope is recorded separately in C-019. |
| C-006 | Universal migration wording is unsuitable for current guidance; the current source retains a legacy Enterprise exception (C-020). |
| C-007 | July model prices are superseded by later price-change notices. The static table is removed. |
| C-008 | Cache details are retired with the model-specific cost table; this is a scope reduction, not a claim that the old cache rule is false. |
| C-009 | Preview-based availability guidance is removed. Check live account/model access for each run. |

See the [source-review record](09-source-review-2026-09-17.md) for observations and limitations. Retired IDs must not support new external claims.

## Rules for downstream documents

1. Reference the claim ID next to each material external claim where practical.
2. Preserve qualifiers such as `estimated`, `sampled`, `preview`, `about`, and exact dates.
3. Never convert a Lab inference into an official fact.
4. When a live pricing or help page changes, update this matrix before updating derived documents.
5. Record old values in version history rather than silently rewriting historical evidence.
6. External one-pagers should include only claims whose freshness check passed within the required window.
7. Update both `Accessed` and `Review by` after a human verifies the source.

## Review log

| Version | Date | Reviewer | Change |
|---|---|---|---|
| 0.1 | 2026-07-21 | CAL-001 facilitator review | Initial material-claim mapping and freshness rules |
| 0.2 | 2026-07-21 | Documentation-integrity implementation | Added machine-checkable review dates |
| 0.3 | 2026-09-17 | Codex-assisted source review; proposed for maintainer approval in the pull request | Rechecked active sources, corrected Business seats, withdrew C-005–C-009, added C-019/C-020, and dated historical statistics; checker rules unchanged |
