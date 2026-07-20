# Safety and Authority Boundary

**Case ID:**  
**Approved by:**  
**Effective date:**  

This document defines what the participant, facilitator, and Codex may do during the pilot. It must be accepted before execution.

## 1. Core rule

> Codex may investigate, draft, test in approved non-destructive environments, organize evidence, and recommend actions. It does not receive independent authority to approve, disclose, deploy, purchase, merge, delete, contact third parties, or make consequential decisions.

The accountable human remains responsible for scope, permissions, interpretation, acceptance, and any action outside the pilot workspace.

## 2. Roles

### Participant / workflow owner

May:

- define the business objective;
- provide authorized inputs;
- confirm data handling constraints;
- accept, partially accept, or reject output;
- approve any later real-world use.

Must:

- avoid sharing secrets or unnecessary personal data;
- disclose material changes to source state;
- review consequential claims;
- report failures and rework honestly.

### Facilitator

May:

- help bound the workflow;
- provide templates and prompts;
- observe the run;
- challenge unsupported claims;
- preserve anonymized metrics.

Must not:

- impersonate OpenAI or claim endorsement;
- pressure the participant to buy or upgrade;
- hide failed runs;
- alter acceptance results;
- access systems without explicit permission.

### Codex / agent system

May:

- read authorized materials;
- create drafts and analysis artifacts;
- propose code or configuration changes;
- run approved local or sandboxed checks;
- organize evidence and uncertainties;
- ask for clarification or approval.

Must not be authorized in this pilot to:

- deploy to production;
- merge or approve pull requests;
- send external messages;
- purchase services or consume unbounded spend;
- transfer money or execute trades;
- delete data or repositories;
- change access controls;
- publish security findings;
- make legal, medical, financial, hiring, firing, or disciplinary decisions;
- bypass platform safeguards or authorization boundaries.

## 3. Data boundary

Allowed by default:

- public repositories and public product information;
- synthetic data;
- sanitized requirements;
- anonymized screenshots and logs;
- explicitly approved non-production environments.

Requires case-specific written approval:

- private repositories;
- internal roadmaps;
- customer-derived data;
- proprietary logs;
- regulated or contract-restricted information.

Prohibited in the seed pilot:

- passwords, API secrets, private keys, session tokens;
- unrestricted production databases;
- unnecessary personal data;
- payment-card, medical, or identity documents;
- confidential third-party information without permission.

## 4. Environment boundary

Approved environment(s):

- 

Approved commands or tool classes:

- 

Prohibited commands or actions:

- 

Maximum time budget:

Maximum usage or cost budget:

## 5. Approval checkpoints

Explicit human approval is required before:

- expanding scope;
- adding a new data source;
- running a command with mutation risk;
- testing an external system;
- installing software outside the approved environment;
- sharing artifacts outside the pilot team;
- converting a recommendation into a production action.

Approval must identify the person, action, scope, and timestamp. Silence is not approval.

## 6. Incident and stop protocol

Stop immediately when:

- secrets or personal data are exposed;
- permissions are ambiguous;
- the agent attempts an unapproved external action;
- the current state no longer matches the captured source state;
- unexpected cost or usage growth occurs;
- evidence suggests potential security or safety impact;
- the participant or facilitator withdraws consent.

Record:

1. timestamp;
2. triggering event;
3. action stopped;
4. data or systems affected;
5. containment performed;
6. decision owner;
7. restart conditions, if any.

## 7. Acceptance

- Participant accepts this boundary: `yes / no`
- Facilitator accepts this boundary: `yes / no`
- Reviewer accepts this boundary: `yes / no`

Any exception:

Exception owner:

Expiry date: