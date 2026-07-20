# Measurement and attribution framework

## Purpose

Measure whether the Codex Adoption Lab creates durable, reviewable value rather than merely generating registrations, prompts, or attractive demonstrations.

The framework separates four layers:

```text
Reach → Activation → Value → Commercial outcome
```

A commercial outcome without verified activation is weak evidence. Activation without accepted value is also weak evidence.

## Metric confidence labels

Every reported number should use one label:

- **Verified** — generated from system records or independently inspectable artifacts.
- **Measured** — recorded through a defined process, but not independently audited.
- **Self-reported** — supplied by a participant.
- **Estimated** — calculated from assumptions.
- **Directional** — useful for learning but too weak for a commercial claim.

## North-star metric

### Human-reviewed workflows accepted and repeated within 30 days

A workflow qualifies when:

1. it was a real participant task;
2. its baseline was recorded before execution;
3. Codex produced an inspectable artifact;
4. a human reviewed the output;
5. the output was accepted or partially accepted with reasons;
6. the participant initiated a comparable second workflow within 30 days.

This metric combines activation, quality, and retention.

## Funnel metrics

### Reach

| Metric | Definition |
|---|---|
| Qualified visitor | Reached the pilot page and matched the target role/problem criteria |
| Application completion | Submitted all required screener fields |
| Eligibility rate | Eligible applicants / completed applications |
| Enrollment rate | Enrolled participants / eligible applicants |

### Activation

| Metric | Definition |
|---|---|
| Baseline completion | Participant recorded current workflow, effort, and acceptance criteria |
| First delegation | First bounded Codex task was started |
| First artifact | At least one inspectable artifact was produced |
| Reviewed artifact | A human recorded a review decision |
| Activated participant | Completed the full activation definition in the pilot document |
| Time to first value | Time from enrollment to first accepted or partially accepted artifact |

### Value

| Metric | Definition |
|---|---|
| Artifact acceptance rate | Accepted or partially accepted artifacts / reviewed artifacts |
| Full acceptance rate | Fully accepted artifacts / reviewed artifacts |
| Review burden | Human review and correction time / total baseline human time |
| Estimated time returned | Baseline human time - setup time - review time - rework time |
| Quality delta | Review score versus the participant's baseline artifact, where comparable |
| Scope expansion | Additional useful work completed that was not feasible in the baseline period |
| Failure visibility | Material failures documented / material failures discovered |

### Retention

| Metric | Definition |
|---|---|
| Seven-day repeat | A second comparable workflow starts within seven days |
| Thirty-day repeat | A second comparable workflow starts within thirty days |
| Workflow depth | Number of accepted stages or agents in the repeated workflow |
| Independent completion | Repeat workflow completed without live facilitator intervention |

### Commercial outcomes

| Metric | Definition |
|---|---|
| Plan-selection confidence | Participant rating before and after the pilot |
| Paid conversion | New paid plan started by an eligible participant |
| Expansion | Plus-to-Pro, individual-to-Business, or incremental team-seat movement |
| First API spend | First qualifying paid API usage after activation |
| Eligible net revenue | Revenue after the contractual exclusions in the partnership proposal |
| Cost per activated participant | Total pilot delivery cost / activated participants |
| Cost per retained participant | Total pilot delivery cost / thirty-day repeat participants |

Commercial outcomes should not be called incremental unless a valid comparison method exists.

## Baseline form

Record before the participant starts:

- participant and cohort ID;
- role and experience level;
- current ChatGPT/Codex plan, if voluntarily disclosed;
- prior Codex usage frequency;
- workflow name;
- workflow frequency;
- average human execution time;
- average review or approval time;
- current output format;
- known error or rework rate;
- business consequence of delay or error;
- data sensitivity classification;
- acceptance criteria;
- confidence in the estimate.

## Workflow event model

Recommended events:

```text
participant_eligible
participant_enrolled
baseline_completed
workflow_defined
context_pack_completed
first_task_started
first_artifact_created
artifact_review_started
artifact_accepted
artifact_partially_accepted
artifact_rejected
workflow_completed
outcome_receipt_created
second_workflow_started
second_workflow_completed
plan_decision_recorded
paid_conversion_observed
commercial_expansion_observed
```

Each event should contain:

- participant ID;
- cohort ID;
- workflow ID;
- timestamp;
- source;
- actor type;
- plan category where permitted;
- confidence label;
- evidence reference;
- free-text notes for exceptions.

## Artifact quality rubric

Score each dimension from 0 to 3:

| Score | Meaning |
|---:|---|
| 0 | Unusable or missing |
| 1 | Major corrections required |
| 2 | Useful with bounded corrections |
| 3 | Accepted with only minor or no corrections |

Dimensions:

1. factual accuracy;
2. completeness against scope;
3. traceability to evidence;
4. prioritization quality;
5. actionability;
6. clarity for the intended reader;
7. compliance with task boundaries.

The total score must not hide a critical boundary violation. A single critical violation should trigger separate escalation.

## Time measurement

### Preferred hierarchy

1. timestamped workflow logs;
2. calendar or task records;
3. participant timer;
4. participant estimate after completion.

### Formula

```text
Net time returned
= baseline human execution time
- participant setup time
- human review time
- correction and rework time
- facilitator time attributable to that participant
```

Report both participant time returned and total operating time. A workflow can save the participant time while remaining too expensive to facilitate at scale.

## Cost-per-workflow model

```text
Total workflow cost
= subscription allocation
+ incremental credits or API usage
+ participant setup cost
+ reviewer cost
+ facilitator cost
+ failure and rework cost
```

```text
Cost per accepted outcome
= total workflow cost / accepted workflows
```

Where exact token or credit data are unavailable, label the value as estimated and publish assumptions.

## Value model

```text
Estimated workflow value
= time returned × loaded hourly cost
+ avoided rework value
+ avoided delay value
+ accepted scope-expansion value
- workflow cost
```

Avoided defects or revenue improvements should be counted only when a defensible causal link exists. Otherwise report them as potential impact, not realized value.

## Attribution designs

### Randomized holdout

Eligible participants are randomly assigned to guided adoption or a comparison experience.

**Strength:** strongest estimate of incrementality.  
**Risk:** requires sufficient sample size and operational approval.

### Matched cohort

Compare participants with similar role, prior usage, plan, geography, and intent.

**Strength:** practical for partner pilots.  
**Risk:** unobserved differences remain.

### Historical baseline

Compare the same segment before and after the intervention.

**Strength:** easy to operate.  
**Risk:** product releases, pricing changes, seasonality, and other campaigns can distort results.

### Referral attribution

Use a referral, campaign, or cohort identifier.

**Strength:** clear association.  
**Risk:** does not prove the participant would not have converted anyway.

## Revenue-share calculation

Only use this calculation after written agreement:

```text
Eligible net revenue
= attributed gross revenue
- taxes
- refunds
- chargebacks
- promotional credits
- pre-existing contracted spend
- excluded products or accounts
```

```text
Performance fee
= eligible incremental net revenue
× agreed percentage
```

Required controls:

- fixed cohort start and end dates;
- account deduplication;
- existing-customer rules;
- attribution hierarchy;
- conversion and revenue lag rules;
- cancellation and refund adjustments;
- payment cap;
- audit and dispute process.

## Pilot dashboard

Minimum dashboard:

| Layer | Metric |
|---|---|
| Cohort | enrolled, eligible starters, completed baselines |
| Activation | first artifacts, reviewed artifacts, activated participants |
| Value | acceptance rate, time returned, review burden, quality score |
| Retention | seven-day and thirty-day repeats |
| Commercial | plan decisions, observed conversion, expansion, API use |
| Operations | facilitator hours, support tickets, cost per activation |
| Safety | critical violations, data incidents, unauthorized attempts |

## Example evidence statement

> Fourteen participants completed a baseline and started a workflow. Nine reached a human-reviewed outcome within seven days, producing a measured activation rate of 64%. Seven reported positive time savings, but only four had timestamped records sufficient for a measured time-return calculation. No conclusion about incremental subscription revenue can be made because the cohort had no comparison group and billing data was unavailable.

This style is more useful than a stronger but unsupported marketing claim.

## Reporting cadence

- daily operational check during Build Week;
- end-of-week activation report;
- two-week failure and repeat-use check;
- thirty-day retention report;
- final commercial analysis only after the attribution window is mature.

## Privacy and retention

Before collecting participant data, document:

- lawful and consent basis;
- minimum necessary fields;
- access roles;
- storage location;
- retention period;
- deletion process;
- anonymization standard;
- publication permissions;
- incident procedure.

Do not collect sensitive source material merely to improve the richness of a case study.
