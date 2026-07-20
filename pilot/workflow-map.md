# QA / Product Audit Workflow Map

**Case ID:**  
**Workflow owner:**  
**Reviewer:**  
**Repository or product:**  
**Exact source state:** branch, commit SHA, build, URL, version, or dated snapshot.

## 1. Bounded objective

Complete this sentence:

> Investigate ________ so that ________ can decide ________, producing ________ by ________.

### In scope

- 
- 
- 

### Out of scope

- 
- 
- 

### Stop conditions

Stop and escalate when:

- the source state changes materially;
- credentials or sensitive data appear unexpectedly;
- production mutation is required;
- authorization is unclear;
- evidence contradicts the task premise;
- a finding could cause harm if disclosed or acted on incorrectly;
- the remaining work exceeds the agreed time or usage budget.

## 2. Inputs

| Input | Exact version / date | Owner | Permission | Sensitive? | Evidence location |
|---|---|---|---|---|---|
| Requirements | | | | | |
| Repository / build | | | | | |
| User journeys | | | | | |
| API specification | | | | | |
| Existing tests | | | | | |
| Analytics / logs | | | | | |

## 3. Workflow stages

### Stage A — Intake and state capture

Deliverables:

- exact source-state record;
- objective, scope, exclusions, and decision owner;
- list of missing information;
- risk classification.

Acceptance gate: the owner confirms the task is bounded and authorized.

### Stage B — Journey and requirement model

Deliverables:

- primary users and goals;
- happy paths;
- alternate and recovery paths;
- states, transitions, dependencies, and permissions;
- requirement conflicts and unknowns.

Each uncertain item must be labeled `unknown`, not converted into a fact.

### Stage C — Risk-based test model

For each risk, capture:

| Risk ID | User or business harm | Trigger | Observable consequence | Test idea | Priority |
|---|---|---|---|---|---|
| R-001 | | | | | |

Priority should consider severity, likelihood, detectability, and reversibility.

### Stage D — Investigation

Permitted actions:

- read and analyze authorized source material;
- run non-destructive tests in an approved environment;
- draft test cases, scripts, queries, and reproduction steps;
- inspect outputs, logs, diffs, screenshots, and network traces;
- propose changes without applying consequential changes.

For every material observation, preserve:

- timestamp;
- exact source state;
- action performed;
- expected result;
- actual result;
- evidence reference;
- limitations.

### Stage E — Findings

Use one record per finding:

| Field | Required content |
|---|---|
| Finding ID | Stable identifier |
| Title | Observable problem, not speculation |
| State | Exact build, SHA, URL, or date |
| Preconditions | Reproducible setup |
| Steps | Minimum reliable sequence |
| Expected | Grounded expectation and source |
| Actual | Observed result |
| Evidence | Stable reference |
| User impact | Direct effect, separated from inference |
| Severity | Defined rubric |
| Confidence | high / medium / low |
| Counterevidence | Any evidence against the conclusion |
| Recommended next action | Investigation, fix, test, or decision |

### Stage F — Prioritized backlog

Separate:

- confirmed defects;
- product opportunities;
- usability friction;
- security or privacy concerns requiring authorized handling;
- unanswered questions;
- rejected hypotheses.

Do not combine all observations into a single severity ranking.

### Stage G — Executive report

The report must contain:

1. objective and exact source state;
2. methods and constraints;
3. confirmed findings;
4. hypotheses and unknowns;
5. business and user implications;
6. recommended actions by urgency;
7. evidence index;
8. acceptance and rejection notes;
9. time and cost measurement.

## 4. Required human gates

| Gate | Accountable human | Decision |
|---|---|---|
| Scope approval | | approve / revise / stop |
| Permission approval | | approve / revise / stop |
| Finding validation | | accept / partial / reject |
| Severity approval | | accept / change |
| External disclosure | | approve / prohibit |
| Production action | | outside pilot |
| Final artifact acceptance | | accept / partial / reject |

## 5. Completion definition

The workflow is complete only when:

- every material claim is linked to evidence or marked as inference;
- failures and rejected findings remain visible;
- review and rework time are recorded;
- the reviewer has issued an acceptance status;
- an outcome receipt has been created.