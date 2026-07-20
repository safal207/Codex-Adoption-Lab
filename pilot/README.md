# Pilot Kit v0.1

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
2. Capture the human baseline in [`baseline-form.md`](baseline-form.md).
3. Select and bound the workflow using [`workflow-map.md`](workflow-map.md).
4. Confirm the authority rules in [`safety-boundary.md`](safety-boundary.md).
5. Run the workflow and preserve evidence.
6. Score the result with [`acceptance-rubric.md`](acceptance-rubric.md).
7. Issue an [`outcome-receipt.md`](outcome-receipt.md).
8. Collect follow-up data using [`follow-up-form.md`](follow-up-form.md).
9. Record metrics and failures in the `evidence/` directory.

## Minimum evidence package per case

Each case must contain:

- anonymized participant ID;
- workflow definition and exclusions;
- baseline estimate and estimation method;
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

## Non-affiliation notice

Codex Adoption Lab is an independent initiative. It is not affiliated with, sponsored by, or endorsed by OpenAI.