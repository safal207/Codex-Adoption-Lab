# Metric Dictionary

This document defines the pilot metrics before data collection. Changes require a dated revision and must not be applied silently to earlier cases.

## Measurement principles

1. Count accepted outcomes, not impressive-looking activity.
2. Separate agent runtime from human active time and elapsed time.
3. Report negative and rejected outcomes.
4. Keep self-reported, calculated, and verified values distinct.
5. Do not infer revenue causality from intent, correlation, or a referral click alone.
6. Use one denominator consistently for each reported rate.

## Core metrics

### Screened participants

**Definition:** Unique people who completed the participant screener.

**Unit:** people  
**Evidence:** completed screener  
**Exclusions:** duplicate submissions and test records.

### Approved cases

**Definition:** Screened workflows approved or approved with constraints.

```text
approval rate = approved cases / screened participants
```

### Started workflows

**Definition:** Approved cases where the participant confirmed the safety boundary and the first workflow action occurred.

### Completed workflows

**Definition:** Started workflows that produced a reviewable final artifact and an acceptance decision.

A run abandoned before review is not complete.

### Activation rate

**Definition:** Percentage of started workflows that reach a reviewable completed artifact within the agreed pilot window.

```text
activation rate = completed workflows / started workflows
```

### Acceptance rate

Report three values:

```text
full acceptance rate = accepted / completed
partial acceptance rate = partially accepted / completed
rejection rate = rejected / completed
```

Do not merge full and partial acceptance without also reporting them separately.

### Time to first value

**Definition:** Elapsed time from the first approved workflow action to the first artifact component the reviewer later accepts.

**Unit:** minutes or hours  
**Evidence:** timestamps plus reviewer mapping  
**Limitation:** depends on reviewer availability and should not be confused with active human time.

### Baseline active human time

**Definition:** Human active work normally required for the comparable workflow before assisted use.

**Source classification:** measured, historical, or estimated.

### Assisted human time

```text
assisted human time = setup time + review time + rework time
```

Do not include unattended agent runtime as human time.

### Net human time saved

```text
net human time saved = baseline active human time - assisted human time
```

Report negative values. Never floor the result at zero.

### Time-saved rate

```text
time-saved rate = net human time saved / baseline active human time
```

Do not calculate when the baseline is zero or materially unreliable.

### Rework ratio

```text
rework ratio = human rework time / assisted human time
```

A high rework ratio may indicate low-quality output even when total time is lower.

### Finding precision

For finding-based workflows:

```text
accepted-finding precision = fully accepted findings / reviewed candidate findings
```

Also report partial and rejected counts. This is not recall.

### Material omission count

**Definition:** Important item the agreed workflow should have surfaced but the reviewer discovered only during or after review.

### Evidence coverage

```text
evidence coverage = material claims with stable evidence or explicit inference label / all material claims
```

Target for a completed case: 100%.

### Safety violation count

**Definition:** Attempted or completed action outside the approved authority, data, environment, or disclosure boundary.

Report severity and whether the action was blocked before impact.

### Day-7 repeat rate

```text
day-7 repeat rate = participants completing another real Codex workflow within 7 days / eligible completed participants
```

Exclude participants who withdrew follow-up consent from the denominator and disclose the exclusion.

### Day-30 retained workflow rate

```text
day-30 retained workflow rate = participants using Codex for a real workflow during days 8–30 / eligible completed participants
```

### Plan-selection confidence

Participant score from 1 to 5 after the pilot. Report distribution and median, not only average.

### Verified plan change

A change supported by evidence the participant voluntarily provides. Verification alone does not establish attribution.

### Attributable conversion

A verified conversion counted only under a pre-agreed measurement contract that defines:

- eligible cohort;
- baseline or holdout;
- tracking method;
- conversion event;
- attribution window;
- prior and concurrent touch exclusions;
- refund and cancellation handling;
- duplicate handling;
- source of truth.

The seed cohort does not report attributable conversion.

### Estimated workflow value

```text
estimated workflow value = labor value of net time saved
                         + verified avoided direct cost
                         - tool and usage cost
                         - facilitator cost
                         - correction cost
```

Speculative risk avoidance must be reported separately.

## Recommended dashboard

Report at minimum:

- screened, approved, started, completed;
- accepted, partially accepted, rejected;
- median time to first value;
- median net human time saved with range;
- median rework ratio;
- evidence coverage;
- safety violations;
- day-7 repeat rate;
- day-30 retained workflow rate;
- failures by category;
- baseline-confidence distribution.

## Revision log

| Version | Date | Change | Reason | Applies from case |
|---|---|---|---|---|
| 0.1 | 2026-07-21 | Initial seed-pilot definitions | Freeze before first cohort | First pilot case |