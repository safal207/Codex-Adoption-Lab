# Failure Register

Failures are first-class pilot evidence. Record them even when the final workflow is accepted.

## Severity

- `F1 — friction`: recoverable confusion or delay with no material output impact.
- `F2 — rework`: incorrect or incomplete output requiring meaningful human correction.
- `F3 — invalid result`: the main artifact or finding cannot be used for the agreed purpose.
- `F4 — boundary incident`: attempted or completed violation of authority, permission, data, environment, cost, or disclosure limits.

## Failure categories

- `intake ambiguity`
- `missing input`
- `source-state drift`
- `environment failure`
- `tool limitation`
- `model or reasoning error`
- `unsupported claim`
- `false positive`
- `material omission`
- `scope drift`
- `excessive review burden`
- `cost overrun`
- `privacy or data handling`
- `authority boundary`
- `participant misunderstanding`
- `facilitator process error`
- `measurement failure`
- `other`

## Register

| Failure ID | Case ID | Timestamp | Severity | Category | Stage | What happened | Expected behavior | Impact | Detected by | Containment | Resolution | Human rework min | Recurrence risk | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| F-001 | | | | | | | | | | | | | | |

## Required incident detail for F4

For every boundary incident, record:

1. approved boundary;
2. attempted or completed action;
3. whether execution was blocked;
4. data or systems affected;
5. immediate containment;
6. person with decision authority;
7. notification or disclosure requirement;
8. conditions for restart;
9. preventive change.

## Root-cause review

Do not stop at “the AI made a mistake.” Classify contributing causes:

- task definition;
- missing context;
- stale or inconsistent source state;
- inadequate permissions model;
- prompt or workflow design;
- tool availability;
- model capability;
- insufficient human review;
- facilitator intervention;
- metric definition;
- participant expectation.

## Corrective-action statuses

- `open`
- `contained`
- `mitigated`
- `accepted risk`
- `not reproducible`
- `closed`

## Pilot-level summary

At each cohort review, publish:

- failures by severity and category;
- cases affected;
- median and total failure-related rework;
- repeated failures;
- new stop conditions;
- templates or workflow rules changed;
- unresolved risks.

Do not remove a failure because a later retry succeeds.

## Revision log

| Version | Date | Change | Reason |
|---|---|---|---|
| 0.1 | 2026-07-21 | Initial failure taxonomy and register | Freeze before seed cohort |