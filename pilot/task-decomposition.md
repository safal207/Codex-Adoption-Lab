# Agent Task Decomposition Template

Break one approved workflow into bounded tasks with explicit inputs, outputs, evidence, and human gates.

**Case ID:**  
**Workflow:**  
**Context pack version:**  
**Exact source state:**  
**Prepared by:**  
**Approved by:**

## 1. Decomposition rules

Each task must:

- have one observable outcome;
- use only approved sources, tools, and environments;
- state what the agent may not do;
- produce evidence that a human can inspect;
- expose uncertainty and counterevidence;
- stop before any consequential action requiring human authority.

Parallel tasks must not mutate the same state unless an accountable human explicitly approves the coordination method.

## 2. Task plan

| Task ID | Objective | Inputs / source IDs | Allowed actions | Prohibited actions | Deliverable | Evidence required | Human gate | Budget |
|---|---|---|---|---|---|---|---|---|
| T-001 | | | | | | | | |

## 3. Dependency graph

```text
T-001
  ↓
T-002 ──→ T-004
  ↓         ↑
T-003 ──────┘
  ↓
Human review
```

Replace the example with the actual graph.

### Parallelization decision

- Tasks safe to run in parallel:
- Shared-state risks:
- Merge or synthesis owner:
- Conflict-resolution rule:
- Maximum concurrent tasks:

## 4. Task instruction block

Use this block for every task.

```text
Task ID:
Objective:
Exact source state:
Inputs:
Known requirements:
Unknowns:
Allowed actions:
Prohibited actions:
Required output format:
Evidence required:
Counterevidence to seek:
Stop conditions:
Human approval required after:
Time / usage budget:
```

## 5. Synthesis task

The synthesis step may combine outputs but may not erase disagreement.

Required sections:

1. confirmed observations;
2. partially supported observations;
3. rejected hypotheses;
4. unresolved conflicts;
5. material omissions;
6. recommended next actions;
7. evidence index;
8. limitations.

## 6. Review map

| Output | Reviewer | Review criterion | Accept / partial / reject | Required correction |
|---|---|---|---|---|
| | | | | |

## 7. Execution record

| Task ID | Start | End | Agent runtime | Human intervention | Status | Failure IDs | Artifact reference |
|---|---|---|---:|---:|---|---|---|
| T-001 | | | | | | | |

Statuses:

- `not started`
- `running`
- `blocked`
- `completed`
- `completed with limitations`
- `rejected`
- `stopped`

## 8. Completion gate

The decomposition is complete only when:

- every task has an accountable reviewer or synthesis owner;
- no task contains hidden authority to purchase, disclose, merge, deploy, or mutate production;
- inputs and exact state are recorded;
- evidence requirements are defined;
- budgets and stop conditions are set;
- the final human gate is explicit.

**Status:** `ready / revise / blocked`  
**Approved by:**  
**Timestamp:**
