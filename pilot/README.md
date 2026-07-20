# Pilot Kit v0.2

This directory turns the Codex Adoption Lab strategy into a bounded, repeatable seed pilot for QA, product, and analysis workflows.

## Pilot objective

Help a participant delegate one real, evidence-heavy workflow to Codex, review the result, and measure whether the workflow created accepted value.

The pilot does **not** attempt to prove that Codex replaces a role, guarantees savings, or causes subscription revenue. It tests whether a supervised workflow can produce a useful outcome with measurable economics.

## Recommended seed cohort

- 5 friendly participants for the first run;
- QA engineers, QA leads, product managers, system analysts, or founders;
- one real workflow per participant;
- no production write access required;
- no regulated, highly confidential, or safety-critical data;
- one facilitator and one accountable participant per case.

## Required sequence

1. Complete [`participant-screener.md`](participant-screener.md).
2. Record consent and data constraints in [`participant-consent.md`](participant-consent.md).
3. Select one eligible workflow using [`first-workflow-selector.md`](first-workflow-selector.md).
4. Capture and freeze the human baseline in [`baseline-form.md`](baseline-form.md).
5. Prepare the source and requirement record using [`context-pack.md`](context-pack.md).
6. Select and bound the workflow using [`workflow-map.md`](workflow-map.md).
7. Break the workflow into inspectable tasks using [`task-decomposition.md`](task-decomposition.md).
8. Confirm the authority rules in [`safety-boundary.md`](safety-boundary.md).
9. Pass the hard start gate below.
10. Run the workflow and preserve evidence.
11. Score the result with [`acceptance-rubric.md`](acceptance-rubric.md).
12. Issue an [`outcome-receipt.md`](outcome-receipt.md).
13. Collect follow-up data using [`follow-up-form.md`](follow-up-form.md).
14. Record metrics and failures in the `evidence/` directory.

## Hard start gate

Investigation must not begin until all items are complete:

- [ ] participant and case IDs assigned;
- [ ] screening decision recorded;
- [ ] consent and publication permission recorded;
- [ ] selected workflow and qualified reviewer recorded;
- [ ] baseline method, value, confidence, timestamp, and confirmation frozen;
- [ ] exact source state recorded;
- [ ] context pack approved;
- [ ] task decomposition approved;
- [ ] safety boundary approved;
- [ ] definition of done and stop conditions recorded;
- [ ] time and usage budget recorded.

A missing baseline blocks time-saved and ROI reporting even when the work continues for process-learning purposes.

## Minimum evidence package per case

Each case must contain:

- anonymized participant ID;
- consent and publication level;
- workflow definition and exclusions;
- baseline value, method, confidence, and frozen timestamp;
- exact source state;
- exact start and finish timestamps;
- agent runtime where available;
- human setup, review, and rework time;
- output artifacts or stable references;
- claim-to-evidence map;
- acceptance result;
- failure log;
- participant follow-up.

## Commercial gate

Do not use the seed cohort as proof of attributable revenue. A partnership or performance-compensation proposal should wait until:

- at least 5 workflows are completed;
- at least 3 are accepted or partially accepted;
- metric definitions remain stable;
- failures are disclosed;
- no participant is counted twice across activation, retention, or expansion metrics;
- any later revenue attribution method is agreed before the measured campaign begins.

## Status labels

Use one status per case:

- `screening`
- `approved`
- `running`
- `review`
- `accepted`
- `partially-accepted`
- `rejected`
- `withdrawn`

## Internal validation case

The first process-validation case is [`CAL-001`](../evidence/cases/CAL-001/case-record.md). It deliberately reports no time savings because the baseline was not frozen before assisted work began.

## Non-affiliation notice

Codex Adoption Lab is an independent initiative. It is not affiliated with, sponsored by, or endorsed by OpenAI.
