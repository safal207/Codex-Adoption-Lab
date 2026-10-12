# Partial source inspection — 2026-10-12

**State: HOLD — human source verification pending.** Assistant inspection date: 2026-10-12 UTC. Starting and observed default-branch SHA: `71e80a170cb3cb494249108553dc1f383bbe5055`. This record proposes corrections; it does not assert human verification or renew the active matrix's freshness dates.

## Source observations

Official pages were opened and relevant content inspected through web retrieval, rather than relying on search snippets. No exact publication date is inferred from relative update labels. Successful content retrieval is separate from the checker's HTTP probe.

| Claim | Source and section inspected | Observation and proposed disposition | Limits |
|---|---|---|---|
| C-001 | [Codex pricing](https://developers.openai.com/codex/pricing/) redirected to [ChatGPT Learn pricing](https://learn.chatgpt.com/docs/pricing), Pricing options and usage FAQ | Codex is included in Free, Go, Plus, Pro, Business, Edu, and Enterprise. Free/Go desktop access is subject to rollout. Replace the old Pro “maximum tasks” description with tier-dependent usage. | Actual access and limits depend on plan, model, task, surface, account, and rollout. Do not promise fixed task counts. No account entitlement was tested. |
| C-002 | [Business overview](https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/) redirected to [current overview](https://help.openai.com/en/articles/8792828-chatgpt-business-overview), seat table and Standard seats | Reconfirmed USD per user/month: Standard $20 annual billing / $25 monthly; Premium $100 annual / $125 monthly. Minimum two Standard/Premium seats combined; mixing is permitted. | Annual values are monthly equivalents billed annually. Regional/currency pricing may differ. Seats are paid capacity, distinct from assigned members. API usage is separately billed. No purchase or quote was obtained. |
| C-019 | [Rate card](https://help.openai.com/en/articles/11481834) redirected to [current credit-based rate card](https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing), Overview and ChatGPT Work and Codex | Work/Codex model usage is priced in credits per million input, cached-input, and output tokens in Standard mode under flexible Business/Enterprise/Edu credit billing. Make the billing scope explicit in the market audit. | Included limits precede purchased credits for Standard Business seats. Eligible legacy Codex-only seats require credits from first use. Legacy Enterprise exceptions remain. Enterprise agreements billed in USD use their own rate card; API and personal-plan pricing must be checked separately. The rate card names Standard Business/eligible Codex-only seats; do not infer Premium billing details from that list alone. No customer's agreement was examined. |
| C-014 | [Partner announcement](https://openai.com/index/introducing-openai-partner-network/), How the network works; [program page](https://openai.com/business/partners/), outcomes and enrollment | Tier progression emphasizes sales performance, technical capability, co-sell engagement, and deployment experience. Program materials also emphasize industry expertise, customer relationships, and delivery capacity. | Distinguish tier criteria from enrollment consideration. Public program descriptions establish neither Lab qualification nor membership, certification, endorsement, or permission to use OpenAI branding. No application or affiliation claim is made. |

## Freshness and completion gate

The [existing contract](08-documentation-integrity.md) requires a human to open the official source, verify/revise the claim, then update `Accessed` and `Review by`. Matrix rule 7 likewise requires human verification. Assistant inspection and user authorization to make changes are not evidence that this happened.

Consequently all four active dates remain unchanged. C-001/C-002/C-019 expired October 5; C-014 is due October 12 and expires October 13. Nothing is removed from the freshness denominator or reclassified to bypass it.

After a human confirms these scoped observations and records reviewer identity/date, apply the verified wording and set `Accessed` to the actual human verification date. If verified October 12, the existing weekly windows propose October 19 for C-001/C-002/C-019 and the fortnightly window proposes October 26 for C-014. These are conditional proposals, not approved deadlines. Before-use review requirements remain. If verification occurs later, calculate from that actual date and re-open volatile sources.

Other claims were not renewed. C-003/C-004/C-020 retain prior deadlines; inspecting overlapping source content does not silently approve them. C-005–C-009 remain retired.

## PR #12 and agreement evidence

[PR #12](https://github.com/safal207/Codex-Adoption-Lab/pull/12) merged September 28 at the starting SHA. The [owner's pre-merge COMMENTED review](https://github.com/safal207/Codex-Adoption-Lab/pull/12#pullrequestreview-5344750243), on `2ee825649eca05cd91d2719e59a4577cec45d958`, explicitly records merge authorization without claiming independent human source verification. The other submitted review was automated COMMENTED output, not human approval. Current draft/pending-merge language is corrected; historical review-time status remains labeled historical.

## Verification

Checker code, tests, workflow, permissions, domain allowlist, and expiry policy are unchanged. The original [failed run](https://github.com/safal207/Codex-Adoption-Lab/actions/runs/38268936075) is historical; it is not rerun as proof of a different revision. Local results and the new PR's CI are recorded in the PR description. HTTP 403 remains BLOCKED, never evidence of page contents. A source-content read does not clear a blocked probe.
