# Example Case — QA / Product Audit

> **Status:** synthetic demonstration only. The numbers below illustrate how to complete the pilot artifacts. They are not results from a real participant and must not be used as evidence of Codex performance, adoption, revenue, or time savings.

**Case ID:** DEMO-001  
**Participant:** synthetic mid-level QA engineer  
**Product:** fictional subscription-management web application  
**Workflow:** audit cancellation and recovery journeys  
**Source state:** fictional build `demo-2026-07-21`  
**Final status:** partially accepted

## 1. Objective

Investigate the cancellation journey so that the product owner can decide which issues should enter the next sprint, producing:

- a journey and state map;
- a risk-based test model;
- evidence-backed findings;
- a prioritized backlog;
- a short executive report.

### In scope

- account owner cancellation;
- cancellation confirmation;
- access until billing-period end;
- failed cancellation request;
- recovery and retry;
- mobile web and desktop web.

### Out of scope

- payment-provider settlement;
- refunds;
- administrator cancellation;
- production access;
- security exploitation.

## 2. Baseline

Baseline method: participant estimate supported by one comparable audit.

| Stage | Human-only active time |
|---|---:|
| Intake and clarification | 30 min |
| Journey mapping | 60 min |
| Test-model creation | 90 min |
| Investigation | 180 min |
| Findings and backlog | 90 min |
| Report | 60 min |
| Review and correction | 45 min |
| **Total** | **555 min** |

Baseline confidence: `3 / 5`.

## 3. Assisted run

| Measure | Time |
|---|---:|
| Human setup | 40 min |
| Unattended agent runtime | 75 min |
| Human review | 80 min |
| Human rework | 55 min |
| **Assisted active human time** | **175 min** |
| **Elapsed time** | **250 min** |

Illustrative net human time saved:

```text
555 - 40 - 80 - 55 = 380 minutes
```

Because this is a synthetic example, the value is not evidence.

## 4. Candidate findings

### DEMO-F-01 — Cancellation confirmation hides the effective end date

**Expected:** The user can see when access ends before confirming cancellation.  
**Actual:** The fictional confirmation dialog says only “Your plan will be cancelled.”  
**Evidence:** Synthetic screenshot reference `demo/evidence/cancel-dialog.png`.  
**Impact:** The user may not understand whether access stops immediately or at period end.  
**Confidence:** high.  
**Reviewer decision:** accepted.  
**Severity adjustment:** medium → medium.

### DEMO-F-02 — Retry action duplicates a cancelled request

**Expected:** A retry after a simulated timeout should resolve the existing request or show its state.  
**Actual:** The synthetic environment creates a second visible cancellation request.  
**Evidence:** Synthetic trace `demo/evidence/retry-trace.json`.  
**Impact:** Potential inconsistent state and support burden.  
**Confidence:** medium.  
**Reviewer decision:** partially accepted because the environment did not model the billing service and the consequence was inferred.

### DEMO-F-03 — Mobile layout prevents cancellation

**Expected:** The cancellation control remains accessible on a narrow viewport.  
**Actual:** Initial agent report claimed the control was hidden.  
**Counterevidence:** Human review found it below the fold and reachable by scrolling.  
**Reviewer decision:** rejected false positive.

## 5. Acceptance scoring

| Dimension | Score 0–4 | Notes |
|---|---:|---|
| Scope fidelity | 4 | Stayed within the defined journey |
| Evidence traceability | 3 | One inference needed clearer labeling |
| Correctness | 3 | One of three findings was rejected |
| Completeness | 3 | Refund boundary correctly excluded |
| Prioritization | 3 | Useful but needed severity correction |
| Decision usefulness | 4 | Backlog was directly reusable |
| Reproducibility | 3 | Synthetic state was preserved |
| Safety compliance | 4 | No external or production action |

Weighted score: `3.35 / 4`.

A score above the full-acceptance threshold would normally qualify, but the reviewer selected **partially accepted** because a candidate finding was materially incorrect and one finding required narrower impact language. The participant's judgment takes precedence over mechanical scoring.

## 6. Failure register entries

| Failure ID | Severity | Category | What happened | Impact | Correction |
|---|---|---|---|---|---|
| DEMO-FAIL-01 | F2 | false positive | Below-the-fold control was reported as inaccessible | One rejected finding | Added viewport and scroll verification step |
| DEMO-FAIL-02 | F1 | unsupported claim | Potential billing impact was phrased too confidently | Review friction | Changed impact to explicit inference |
| DEMO-FAIL-03 | F1 | participant misunderstanding | Reviewer initially counted agent runtime as human time | Inflated assisted cost | Clarified metric dictionary |

## 7. Outcome receipt summary

- Candidate findings: 3
- Accepted: 1
- Partially accepted: 1
- Rejected: 1
- Evidence coverage after correction: 100%
- Safety violations: 0
- Synthetic net human time saved: 380 minutes
- Final artifact status: partially accepted
- Recommended workflow change: require an explicit interaction check before reporting a responsive-layout blocker.

## 8. Claims permitted from this example

Permitted:

- the repository contains a runnable measurement method;
- the method records false positives, rework, and negative results;
- the templates distinguish human time from agent runtime.

Not permitted:

- Codex saved 380 minutes in a real audit;
- the workflow achieved a particular precision rate in production;
- the example caused a subscription purchase or business outcome;
- OpenAI reviewed or endorsed the method.