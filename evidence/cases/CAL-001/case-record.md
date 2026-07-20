# CAL-001 — Internal partner-readiness audit

**Case ID:** `CAL-001`  
**Workflow:** QA / Product Audit of the Codex Adoption Lab evidence package  
**Participant / owner:** Repository owner  
**Facilitator:** Codex-assisted review  
**Run date:** 2026-07-21  
**Exact audited state:** `a78a5c7fa05cdab877c73fe5aaab8007a3cb8a41`  
**Source branch:** `agent/pilot-kit-v0.1`  
**Final owner decision:** `partially accepted`  
**Owner sign-off date:** 2026-07-21

This is a real internal process-validation case. It is not a testimonial, revenue proof, or evidence that an external cohort will achieve the same result.

## 1. Suitability decision

- Real workflow: yes — determine whether the repository is ready to support seed execution and later partner outreach.
- Qualified reviewer: repository owner.
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

> Investigate the Codex Adoption Lab strategy and pilot package so that the repository owner can decide whether it is credible enough for a seed cohort and later partner outreach, producing a prioritized audit, corrections, and an outcome receipt.

### In scope

- README and repository navigation;
- market, pricing, adoption, and partnership claims;
- internal education and activation strategy;
- runnable pilot templates;
- claim traceability;
- safety and authority boundaries;
- commercial and attribution logic.

### Out of scope

- OpenAI internal data or roadmap;
- legal approval of commercial terms;
- submission to the Partner Network;
- external participant recruitment;
- empirical productivity or conversion claims;
- production code or customer systems.

## 3. Baseline record

The protocol requires a human-only baseline to be frozen before assisted work begins. That did not happen for CAL-001.

- Baseline method: unavailable
- Baseline active human time: not measured
- Baseline confidence: `0 — invalid for comparison`
- Time-saved calculation: prohibited
- ROI calculation: prohibited

This is recorded as failure `CAL-001-F1`. No retrospective estimate is inserted as if it had been frozen before the run.

Protocol correction for later cases:

> A case may not move from intake to investigation until the baseline form contains a method, active-time value, confidence score, timestamp, and accountable confirmation.

## 4. Authority and safety boundary

Permitted:

- read the exact public repository state;
- compare claims with official public sources;
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

Observed safety or authority violations: `0`.

## 5. Evidence inspected

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

- ChatGPT pricing
- ChatGPT Business pricing
- Codex rate card
- Codex flexible-pricing and availability materials
- Codex knowledge-work and agent-adoption reports
- GPT-5.6 pricing and availability materials
- OpenAI Partner Network materials

Material claims are mapped in `docs/06-claim-evidence-matrix.md`.

## 6. Findings and remediation

### CAL-001-01 — API cache pricing was materially ambiguous

**Severity:** high  
**Confidence:** high  
**Status:** mitigated in PR #5

The original market audit collapsed cache reads and cache writes under one label. The remediation separates uncached input, cache writes, cache reads, output, and API availability status.

### CAL-001-02 — Material claims lacked claim-level traceability

**Severity:** high  
**Confidence:** high  
**Status:** mitigated in PR #5

The original package used document-level source lists. The remediation adds `docs/06-claim-evidence-matrix.md` with claim IDs, classifications, sources, access dates, qualifiers, and freshness rules.

### CAL-001-03 — Promised pilot deliverables were missing as runnable assets

**Severity:** medium  
**Confidence:** high  
**Status:** mitigated in PR #5

The remediation adds:

- `pilot/first-workflow-selector.md`;
- `pilot/context-pack.md`;
- `pilot/task-decomposition.md`;
- `pilot/participant-consent.md`.

### CAL-001-04 — Partner-entry strategy underweighted the eligibility gap

**Severity:** medium  
**Confidence:** medium  
**Status:** mitigated in PR #5

The remediation adds a two-path strategy: first produce seed evidence and explore bounded co-delivery; apply directly only after delivery evidence and operating controls exist.

### CAL-001-05 — External narrative risked leading with methodology

**Severity:** low  
**Confidence:** medium  
**Status:** mitigated in PR #5

External language now emphasizes workflow adoption, accepted outcomes, safety, and evidence. The Product Launch Formula inspiration remains internal design rationale.

### CAL-001-06 — No automated freshness or link-integrity control

**Severity:** low  
**Confidence:** high  
**Status:** open in issue #6

The package still requires a documentation-integrity check before external publication.

## 7. Failure register

| Failure ID | Severity | Category | Impact | Containment | Status |
|---|---|---|---|---|---|
| CAL-001-F1 | F2 | measurement failure | No valid time-saved or ROI calculation | Prohibit savings and ROI claims; add hard baseline gate | contained |
| CAL-001-F2 | F2 | unsupported claim structure | Evidence had to be reconstructed manually | Add claim-evidence matrix | mitigated in PR #5 |
| CAL-001-F3 | F2 | missing operational assets | Facilitator improvisation would reduce reproducibility | Add selector, consent, context, and decomposition templates | mitigated in PR #5 |
| CAL-001-F4 | F1 | pricing terminology | Cost interpretation could be misleading | Split cache read/write and availability language | mitigated in PR #5 |

## 8. Acceptance review

Scores apply to the exact audited state, before remediation.

| Dimension | Weight | Score | Weighted score |
|---|---:|---:|---:|
| Scope fidelity | 15% | 4.0 | 0.60 |
| Evidence traceability | 20% | 2.0 | 0.40 |
| Factual and technical correctness | 20% | 3.0 | 0.60 |
| Completeness for the agreed purpose | 10% | 2.5 | 0.25 |
| Prioritization quality | 10% | 3.5 | 0.35 |
| Clarity and decision usefulness | 10% | 4.0 | 0.40 |
| Reproducibility | 10% | 3.0 | 0.30 |
| Safety and authority compliance | 5% | 4.0 | 0.20 |
| **Total** | **100%** |  | **3.10 / 4.00** |

**Final owner decision:** `partially accepted`.

Accepted use:

- internal strategy and pilot development;
- remediation through PR #5;
- preparation for a controlled seed cohort after integrity controls are added.

Prohibited use:

- claiming a validated adoption or revenue system;
- sending a performance-based proposal as proven;
- publishing time-saved or ROI numbers from CAL-001;
- implying OpenAI endorsement or Partner Network eligibility.

## 9. Outcome receipt

### Delivered artifacts

| Artifact | Status | Accepted use |
|---|---|---|
| Partner-readiness audit | accepted for internal use | Prioritization and remediation |
| Claim verification | partially accepted | Current-fact review with freshness controls pending |
| Failure register | accepted | Process improvement |
| Acceptance scoring | accepted as assessment of the audited state | Owner decision support |
| Time and ROI receipt | invalid | No savings or economic claim |

### Quality receipt

- Weighted score: `3.10 / 4.00`
- Material findings: `6`
- Confirmed defects or gaps: `4`
- Strategic risks or recommendations: `2`
- Safety or authority violations: `0`

### Economics

Not calculated. No revenue, conversion, avoided-loss, labor-value, time-saved, or ROI claim is permitted from CAL-001.

## 10. Owner sign-off

- Accountable reviewer: repository owner
- Final decision: `partially accepted`
- Decision date: 2026-07-21
- Permitted external claim: the Lab completed one internal process-validation audit and retained its negative measurement result
- Claims that must not be made: time savings, ROI, revenue impact, OpenAI endorsement, Partner Network acceptance, or external-user validation
- Next gate: complete issue #6, then run four additional real seed cases with frozen baselines
