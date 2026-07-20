# CAL-001 — Internal partner-readiness audit

**Case ID:** `CAL-001`  
**Workflow:** QA / Product Audit of the Codex Adoption Lab evidence package  
**Participant / owner:** Repository owner  
**Facilitator:** Codex-assisted review  
**Run date:** 2026-07-21  
**Exact source state:** `a78a5c7fa05cdab877c73fe5aaab8007a3cb8a41`  
**Source branch:** `agent/pilot-kit-v0.1`  
**Provisional status:** `partially accepted — owner sign-off pending`

This is a real internal process-validation case. It is not a testimonial, revenue proof, or evidence that an external cohort will achieve the same result.

## 1. Suitability decision

- Real workflow: yes — determine whether the repository is ready to support partner outreach.
- Qualified reviewer available: repository owner, final sign-off pending.
- Stable source state: yes, exact commit captured above.
- Sensitive production data required: no.
- Production mutation required: no.
- High-impact autonomous action required: no.
- Result: `approved with constraints`.

Constraints:

1. review public repository content only;
2. use official public OpenAI sources for current product claims;
3. do not submit a Partner Network form or external message;
4. do not claim OpenAI affiliation;
5. do not claim time savings, conversion, or revenue impact from this case.

## 2. Bounded objective

> Investigate the Codex Adoption Lab strategy and pilot package so that the repository owner can decide whether it is credible enough for a seed cohort and later partner outreach, producing a prioritized audit, corrections, and an outcome receipt on 2026-07-21.

### In scope

- README and repository navigation;
- market, pricing, adoption, and partnership claims;
- PLF-inspired adoption strategy;
- runnable pilot templates;
- claim traceability;
- safety and authority boundaries;
- commercial and attribution logic.

### Out of scope

- OpenAI internal data or roadmap;
- legal approval of revenue-share terms;
- submission to the Partner Network;
- external participant recruitment;
- empirical Codex productivity or conversion claims;
- production code or customer systems.

## 3. Baseline record

The pilot protocol requires a human-only baseline to be frozen before assisted work begins. That did not happen for CAL-001.

**Baseline method:** unavailable  
**Baseline active human time:** not measured  
**Baseline confidence:** `0 — invalid for comparison`  
**Time-saved calculation:** prohibited

This is recorded as failure `CAL-001-F1`. No retrospective estimate will be inserted as if it had been frozen before the run.

Protocol correction for later cases:

> A case may not move from intake to investigation until the baseline form contains a method, active-time estimate or measured value, confidence score, timestamp, and accountable confirmation.

## 4. Authority and safety boundary

Permitted:

- read the exact public repository state;
- compare claims with current official public sources;
- draft findings and corrections on a new branch;
- create a draft pull request;
- propose issues and next actions.

Prohibited:

- merge or deploy without owner approval;
- submit forms or contact OpenAI;
- purchase or recommend a plan as an official OpenAI recommendation;
- expose secrets or private participant information;
- present hypotheses, synthetic examples, or this internal run as market proof;
- choose the final reviewer decision on behalf of the repository owner.

No safety or authority violation was observed during the run.

## 5. Sources inspected

### Repository evidence

- `README.md`
- `docs/01-market-audit.md`
- `docs/02-plf-launch-strategy.md`
- `docs/04-partnership-proposal.md`
- `pilot/baseline-form.md`
- `pilot/workflow-map.md`
- `pilot/acceptance-rubric.md`
- `pilot/outcome-receipt.md`
- exact PR #3 head and dependency chain

### Official public evidence checked on 2026-07-21

- https://chatgpt.com/pricing/
- https://openai.com/business/pricing/
- https://help.openai.com/en/articles/20001106
- https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/
- https://openai.com/index/codex-flexible-pricing-for-teams/
- https://openai.com/index/codex-for-knowledge-work/
- https://openai.com/index/how-agents-are-transforming-work/
- https://openai.com/index/gpt-5-6/
- https://help.openai.com/en/articles/20001325-a-preview-of-gpt-5-6-sol-terra-and-luna/
- https://openai.com/index/introducing-openai-partner-network/
- https://openai.com/business/partners/

## 6. Findings

### CAL-001-01 — API cache pricing is materially ambiguous

**Severity:** high  
**Confidence:** high  
**Status:** confirmed

The market audit presents one `Cached input` price per GPT-5.6 model. Current official information distinguishes:

- uncached input;
- cache writes at `1.25x` uncached input;
- cache reads at a `90%` discount;
- output pricing.

Calling the discounted value simply `Cached input` can lead a reader to treat cache writes and reads as the same charge. The document also calls the values “current standard” pricing without clearly separating ChatGPT availability from API preview status.

**Required correction:** split the table into uncached input, cache write, cache read, and output; label the API status and snapshot date.

### CAL-001-02 — Material claims are not traceable claim by claim

**Severity:** high  
**Confidence:** high  
**Status:** confirmed

The repository has official source lists, but the key pricing, adoption, availability, and Partner Network claims are not mapped to a specific source and access date. This conflicts with the pilot's own completion rule requiring material claims to link to evidence or be labeled as inference.

**Required correction:** add a frozen claim-evidence matrix with claim ID, classification, source, source date, access date, and freshness rule.

### CAL-001-03 — Promised pilot deliverables are missing as runnable assets

**Severity:** medium  
**Confidence:** high  
**Status:** confirmed

The partnership proposal promises:

- a first-workflow selector;
- a context-pack template;
- an agent task-decomposition template.

PR #3 contains references to these concepts but no dedicated runnable files. A facilitator would need to improvise them, reducing reproducibility.

**Required correction:** add all three templates and link them from the pilot navigation.

### CAL-001-04 — Partner-entry strategy underweights the eligibility gap

**Severity:** medium  
**Confidence:** medium  
**Status:** confirmed strategic risk

The public Partner Network emphasizes sales performance, technical capability, co-sell engagement, deployment experience, industry expertise, delivery capacity, and customer relationships. The proposal mentions direct enrollment and existing partners but does not rank the routes based on the Lab's current evidence maturity.

**Required correction:** define a two-path entry strategy:

1. primary near-term path — produce seed evidence and approach an existing listed partner for a bounded co-delivery experiment;
2. secondary path — apply directly after delivery evidence, references, operating controls, and repeatable assets exist.

### CAL-001-05 — The external narrative risks leading with methodology instead of buyer outcome

**Severity:** low  
**Confidence:** medium  
**Status:** product recommendation

The PLF-inspired structure is useful internally, but an OpenAI or implementation-partner conversation is more likely to respond to workflow adoption, measurable outcomes, segment access, and safe delivery than to the Jeff Walker label.

**Required correction:** keep PLF as internal design rationale; use “evidence-based education and activation sequence” in external materials.

### CAL-001-06 — No automated freshness or link-integrity control

**Severity:** low  
**Confidence:** high  
**Status:** confirmed

The package depends on fast-changing pricing, availability, and policy pages. There is no automated link check, source freshness check, or review-by date.

**Required correction:** add a small documentation-integrity check or a manual freshness protocol before external publication.

## 7. Failure register

| Failure ID | Severity | Category | What happened | Impact | Containment | Corrective action | Status |
|---|---|---|---|---|---|---|---|
| CAL-001-F1 | F2 | measurement failure | Baseline was not frozen before assisted investigation began | No valid time-saved metric can be calculated | Prohibit time and ROI claims for CAL-001 | Add hard baseline gate to runbook | contained |
| CAL-001-F2 | F2 | unsupported claim structure | Material claims had document-level source lists but no claim-level mapping | Partner reviewer would need to reconstruct evidence manually | Treat package as partially accepted | Add claim-evidence matrix | open until matrix merged |
| CAL-001-F3 | F2 | missing input / artifact | Three promised operational templates were absent | Pilot could not start without facilitator improvisation | Do not recruit external cohort yet | Add selector, context pack, and decomposition templates | open until assets merged |
| CAL-001-F4 | F1 | pricing terminology | Cache read and write economics were collapsed into one label | Potential buyer cost misunderstanding | Mark current table for correction | Replace pricing table and add status note | open until correction merged |

## 8. Provisional acceptance review

Scores use the frozen rubric from `pilot/acceptance-rubric.md`.

| Dimension | Weight | Score | Weighted score | Notes |
|---|---:|---:|---:|---|
| Scope fidelity | 15% | 4.0 | 0.60 | The package consistently targets QA/Product adoption. |
| Evidence traceability | 20% | 2.0 | 0.40 | Official sources exist, but claim-level mapping is absent. |
| Factual and technical correctness | 20% | 3.0 | 0.60 | Core claims verified; API cache terminology needs correction. |
| Completeness for the agreed purpose | 10% | 2.5 | 0.25 | Key runnable templates are missing. |
| Prioritization quality | 10% | 3.5 | 0.35 | Strong gates and seed-first sequencing. |
| Clarity and decision usefulness | 10% | 4.0 | 0.40 | Clear structure and commercial boundaries. |
| Reproducibility | 10% | 3.0 | 0.30 | Strong forms, but missing assets force improvisation. |
| Safety and authority compliance | 5% | 4.0 | 0.20 | Explicit independent status and human authority boundaries. |
| **Total** | **100%** |  | **3.10 / 4.00** | Below full-acceptance threshold. |

Mandatory full-acceptance gate does not pass because several material claims lack direct claim-level evidence mapping.

**Facilitator recommendation:** `partially accepted`.

Accepted use now:

- internal strategy review;
- development of the pilot kit;
- one controlled internal case;
- preparation for a friendly seed cohort after fixes.

Prohibited use now:

- claiming a validated adoption or revenue system;
- sending a performance-based proposal as proven;
- publishing time-saved or ROI numbers from CAL-001;
- implying Partner Network eligibility or OpenAI endorsement.

## 9. Outcome receipt

### Intended outcome

Determine whether the repository is ready for seed-cohort execution and later partner outreach.

### Delivered artifacts

| Artifact | Status | Accepted use |
|---|---|---|
| Partner-readiness audit | delivered | Internal prioritization and correction |
| Claim verification | delivered with corrections required | Current-fact review only |
| Failure register | delivered | Pilot process improvement |
| Acceptance scoring | provisional | Owner decision support |
| Time and ROI receipt | invalid | No external or internal savings claim |

### Time receipt

No valid human-only baseline exists. Active human time saved, time-saved rate, and economic value are `not calculated`.

### Quality receipt

- Weighted provisional score: `3.10 / 4.00`
- Material findings: `6`
- Confirmed defects or gaps: `4`
- Strategic risks / recommendations: `2`
- Known material omission discovered during review: missing operational templates
- Unsupported-claim structure discovered: claim-level traceability absent
- Safety or authority violations: `0`

### Economics

Not calculated. No revenue, conversion, avoided-loss, or labor-value claim is permitted from CAL-001.

### Reviewer sign-off

- Accountable reviewer: repository owner
- Final decision: pending
- Recommended decision: partially accepted
- Permitted external claims: none from CAL-001 until owner review and sanitization
- Claims that must not be made: time savings, revenue impact, OpenAI endorsement, Partner Network acceptance, external-user validation
