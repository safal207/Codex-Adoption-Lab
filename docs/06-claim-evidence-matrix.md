# Claim–evidence matrix

**Latest source-content inspection and owner attestation:** 2026-11-24 (Moscow time; 2026-11-23 UTC), documented in the [November review and attestation](14-source-review-2026-11-24.md). All 11 active official claims were personally source-verified as reported by the owner in the task conversation. Dates below use UTC. Earlier October review records remain historical.

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

**Source-verification boundary:** the November review supersedes the October 19 proposals for active guidance. The 11 renewed rows are scoped to the owner's explicit personal source-verification attestation; no merge authorization or GitHub APPROVED review is implied. New assistant inspections, green CI or HTTP success alone cannot reset dates.

| Claim ID | Material claim | Classification | Official evidence | Published / updated | Accessed | Review by | Freshness rule |
|---|---|---|---|---|---|---|---|
| C-001 | Codex is included across Free, Go, Plus, Pro, Business, Edu and Enterprise. Desktop Free/Go access depends on rollout; usage and access vary by plan, model and surface. Do not promise a fixed task allowance. | official fact | https://developers.openai.com/codex/pricing/ | live pricing documentation (redirects to ChatGPT Learn; see November 24 record) | 2026-11-23 | 2026-11-30 | Recheck before every external use and at least weekly during a launch. |
| C-002 | Business Standard costs USD 20 per seat/month on annual billing or 25 monthly; Premium costs 100 or 125 respectively. The current signup guide and overview permit one paid Standard or Premium seat for a new workspace. Local price and checkout requirements may differ; confirm at checkout. Codex Pricing still lists 2+ users; the sources disagree, so verify actual checkout rather than guaranteeing one-seat eligibility. | official fact | https://help.openai.com/en/articles/8792828-chatgpt-business-overview and https://help.openai.com/en/articles/8980713-sign-up-for-chatgpt-business and https://developers.openai.com/codex/pricing/ | live help article | 2026-11-23 | 2026-11-30 | Recheck before every external use and at least weekly during a launch. |
| C-003 | Both Standard and Premium Business seats cover ChatGPT, Work and Codex; Premium provides greater usage capacity. API billing is independent. | official fact | https://help.openai.com/en/articles/8792828-chatgpt-business-overview | live help article | 2026-11-23 | 2026-12-23 | Recheck monthly and before a proposal. |
| C-004 | Only eligible Business workspaces that added the legacy Codex-only seat type before June 24, 2026 can retain access to that type. | official fact | https://help.openai.com/en/articles/8792828-chatgpt-business-overview and https://help.openai.com/en/articles/8980713-sign-up-for-chatgpt-business | live help article | 2026-11-23 | 2026-12-23 | Recheck monthly and before any seat recommendation. |
| C-010 | OpenAI reported over five million weekly active Codex users on June 2, 2026; not a current user count. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-11-23 | 2026-12-23 | Keep the publication date; do not present as a current count. |
| C-011 | The same June 2 report estimated knowledge workers at roughly one fifth of users; their growth rate was more than triple developers' growth rate. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-11-23 | 2026-12-23 | Preserve historical framing and approximation. |
| C-012 | In May 2026, 70.2% of sampled individual users submitted at least one request with an estimated human task horizon above one hour. Estimates use an LLM judge on transcripts and queries from a random 0.1% sample; directional rather than exact, not measured time savings or completion rates. | official fact with methodology limitation | https://openai.com/index/how-agents-are-transforming-work/ | 2026-06-25 | 2026-11-23 | 2026-12-23 | Preserve sample, model-estimated duration, and measurement month; do not infer Lab results. |
| C-013 | On June 14, 2026 OpenAI announced a partner program intended to help organizations adopt and deploy AI solutions, including workflow integration and change management. | official fact | https://openai.com/index/introducing-openai-partner-network/ | 2026-06-14 | 2026-11-23 | 2026-12-23 | Recheck monthly and before partner outreach. |
| C-014 | Partner progression through Select, Advanced and Elite considers commercial results, technical strength, joint selling and deployment track record. The public program also seeks sector knowledge, customer relationships and delivery capability; enrollment is consideration, not acceptance. No Lab eligibility or affiliation is implied. | official fact | https://openai.com/index/introducing-openai-partner-network/ and https://openai.com/business/partners/ | live / 2026-06-14 | 2026-11-23 | 2026-12-07 | Recheck at least fortnightly and before enrollment or qualification claims. |
| C-015 | Helping a user complete one accepted workflow before recommending a plan may improve activation and plan confidence. | Lab hypothesis | Supported directionally by C-013; requires experiment | n/a | 2026-07-21 | n/a | Never state as proven until measured. |
| C-016 | The QA/Product segment is an attractive initial wedge because its work is evidence-heavy, reviewable, and repeatable. | Lab inference | Internal workflow analysis; not an OpenAI claim | n/a | 2026-07-21 | n/a | Validate through interviews and seed cases. |
| C-017 | A seven-day Build Week and three-event education sequence can improve activation, retention, or conversion. | Lab proposal | `docs/02-plf-launch-strategy.md` | n/a | 2026-07-21 | n/a | Requires controlled measurement; do not claim causality in advance. |
| C-018 | A 5–10% revenue share could be a negotiation option. | Lab proposal | `docs/04-partnership-proposal.md` | n/a | 2026-07-21 | n/a | Not an OpenAI term or market standard; use only after attribution and procurement review. |
| C-019 | For applicable credit-based flexible workspaces, Work/Codex Standard-mode charges use credits per million input, cached input and output tokens. The rate card specifies eligible Business standard/legacy Codex seat users and credit-based Enterprise/Edu and additional named workspace categories. Included limits, seat-specific treatment, speed multipliers, legacy rates and USD agreements need separate checks; API pricing is separate. Do not infer Premium-specific rates from a section naming standard seats. | official fact | https://help.openai.com/en/articles/11481834 and https://help.openai.com/en/articles/8792828-chatgpt-business-overview | live help article | 2026-11-23 | 2026-11-30 | Recheck weekly and before a budget recommendation. |
| C-020 | Some Enterprise workspaces remain on legacy Codex rates until migrated; the workspace agreement determines applicable credit or USD rates. | official fact | https://help.openai.com/en/articles/11481834 | live help article | 2026-11-23 | 2026-12-23 | Recheck monthly and against the participant's agreement. |

## Retired claim IDs

`C-005` through `C-009` are withdrawn from current guidance as of 2026-09-17. They are not reclassified as hypotheses or silently assigned new expiry dates. Their original wording, access dates, and expired deadlines remain in the [pre-review matrix](https://github.com/safal207/Codex-Adoption-Lab/blob/98a9c273458f6550207e4536648deedfb16c3ff9/docs/06-claim-evidence-matrix.md).

| Retired ID | Disposition |
|---|---|
| C-005 | April transition summary is not supported by the redirected source now; current billing scope is recorded separately in C-019. |
| C-006 | Universal migration wording is unsuitable for current guidance; the current source retains a legacy Enterprise exception (C-020). |
| C-007 | July model prices are superseded by later price-change notices. The static table is removed. |
| C-008 | Cache details are retired with the model-specific cost table; this is a scope reduction, not a claim that the old cache rule is false. |
| C-009 | Preview-based availability guidance is removed. Check live account/model access for each run. |

See the [September 17 source-review record](09-source-review-2026-09-17.md) for the retirement decisions and the [September 28 review](10-source-review-2026-09-28.md) for earlier active-source checks; see the [October 12 record](11-source-review-2026-10-12.md) for the four renewed claims. The [October 19 assistant inspection](12-source-review-2026-10-19.md) and [staged proposal packet](13-proposed-claim-matrix-changes-2026-10-19.md) did not renew dates at that time. The [November 24 review](14-source-review-2026-11-24.md) records the subsequent scoped owner attestation and renewal. Retired IDs must not support new external claims. This pass does not validate the five retired statements.

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
| 0.7 | 2026-10-19 | ChatGPT assistant; source inspection only, fresh owner verification pending | Compared C-001/C-002/C-014/C-019 and C-010–C-012 with official sources; staged proposed replacement text and C-012 methodology in a separate review packet; left active claim wording, `Accessed` and `Review by` dates, retired IDs and CI gate unchanged |
| 0.8 | 2026-11-23 | Aleksey Safonov; explicit personal source-verification attestation in task conversation (November 24 Moscow time) | Renewed C-001–C-004, C-010–C-014, C-019–C-020 with qualifications and conflicting Business minimum-seat guidance preserved; no merge approval, no changes to retired IDs or CI policy. |
