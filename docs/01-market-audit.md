# Codex market and pricing audit

**Snapshot date:** 2026-07-21  
**Scope:** public Codex positioning, personal and business plan ladder, credit mechanics, API economics, and adoption opportunity.

## 1. Confirmed product direction

Codex is no longer presented only as a single coding assistant. Official OpenAI materials describe:

- a desktop command center for managing multiple agents and long-running tasks;
- isolated worktrees for parallel work on the same repository;
- use across app, CLI, IDE, cloud, and mobile;
- mobile review of screenshots, terminal output, diffs, tests, questions, and approvals;
- growing use by analysts, legal teams, recruiting teams, and other knowledge workers;
- movement from short chat interactions to delegated tasks that can run for minutes or hours.

### Adoption signals

OpenAI reported in June 2026 that:

- Codex had more than 5 million weekly active users;
- knowledge workers represented about 20% of users and were growing faster than developer usage;
- in May 2026, more than 70% of users requested at least one task estimated to take a human more than one hour.

These figures support a broader adoption thesis, but they do **not** prove that any specific launch tactic will increase paid conversion. That remains an experiment.

## 2. Current offer ladder

The public ChatGPT plan ladder currently includes:

| Plan | Codex role in the ladder | Primary adoption job |
|---|---|---|
| Free | Limited Codex access | Demonstrate that an agent can complete a real task |
| Go | Limited Codex access on supported experiences | Keep light users engaged before professional adoption |
| Plus | Expanded Codex usage and GPT-5.6 access | Establish a weekly professional workflow |
| Pro | 5x or 20x more usage and maximum Codex tasks | Support intensive, parallel, daily agent work |
| Business | Shared secure workspace, administration, analytics, budgeting, and Codex | Move from individual success to team deployment |
| Enterprise | Custom scale, controls, support, and commercial terms | Govern agentic work in large organizations |

Public prices and local-currency offers can change by region and account. The live pricing page should remain the source of truth for exact personal-plan prices.

### Business pricing

OpenAI currently advertises ChatGPT Business at:

- **$20 per user/month**, billed annually;
- **$25 per user/month**, billed monthly;
- minimum two users.

A notable constraint: starting June 24, 2026, new usage-based Codex-only seats stopped being available to new Business plans and Business workspaces that had never added such a seat before that date. Standard Business seats still include Codex under the plan's current limits and credit mechanics.

## 3. April 2026 pricing transition

The pricing story changed materially in April:

- **April 2, 2026:** Codex pricing moved from approximate per-message pricing toward token-aligned usage for Plus, Pro, Business, and new Enterprise plans.
- **April 23, 2026:** the remaining existing Enterprise plans, including Edu, Health, Gov, and ChatGPT for Teachers, were moved to the updated approach.

The official rate card says Codex commonly costs approximately **$100–$200 per developer per month on average**, with substantial variation based on model choice, number of instances, automations, fast mode, and workload.

### Marketing consequence

Token alignment improves cost traceability, but it also increases cognitive load. A buyer must understand:

- included plan usage;
- credits after included limits;
- model mix;
- cached versus uncached input;
- output-heavy tasks;
- parallel instances and automations.

This is economically rational infrastructure pricing, but it is not yet a simple adoption story for a first-time buyer.

## 4. API price architecture

Current standard GPT-5.6 text-token pricing per 1 million tokens:

| Model | Intended use | Input | Cached input | Output |
|---|---|---:|---:|---:|
| GPT-5.6 Sol | Frontier capability for complex professional work | $5.00 | $0.50 | $30.00 |
| GPT-5.6 Terra | Balance of intelligence and cost | $2.50 | $0.25 | $15.00 |
| GPT-5.6 Luna | Cost-sensitive, high-volume workflows | $1.00 | $0.10 | $6.00 |

Prompts above the published long-context threshold can use different multipliers. Tool calls can add separate charges. Production economics therefore need to be measured per completed workflow, not estimated from headline token prices alone.

## 5. Product-to-market gap

### What the product already communicates well

- Technical capability is credible and expanding.
- Multi-agent and long-running work are differentiated from ordinary chat.
- Security boundaries and approval flows are visible.
- The ladder from individual use to managed enterprise deployment exists.
- Flexible credits reduce the need to upgrade solely because one period is unusually busy.

### Where adoption can still improve

#### Gap A — feature comprehension precedes transformation

A new user encounters models, limits, credits, apps, tasks, worktrees, approvals, hooks, and environments before developing a stable answer to:

> What valuable work should I delegate first?

#### Gap B — plan selection is usage-led rather than outcome-led

The user needs a translation layer:

| User intent | Recommended starting logic |
|---|---|
| Test one real workflow | Start with available included access and measure first value |
| Run a professional workflow every week | Evaluate Plus around repeatability and plan limits |
| Operate multiple demanding tasks daily | Evaluate Pro based on concurrency and sustained usage |
| Deploy across a team | Evaluate Business or Enterprise controls, data policy, and spend governance |
| Embed an agent workflow into a product or internal system | Model API cost per accepted outcome |

This is a decision framework, not an official OpenAI plan recommendation.

#### Gap C — economic proof arrives too late

The first-session experience should help users capture:

- baseline human time;
- agent runtime;
- review time;
- accepted output;
- rework;
- avoided defect or delay;
- repeatability.

Without that measurement, an upgrade feels like buying more AI. With it, an upgrade can feel like funding a proven operating system.

#### Gap D — different professions require different entry stories

A developer, QA lead, product manager, analyst, and founder may use the same platform but do not buy the same transformation.

The initial Lab pilot therefore avoids a universal campaign and begins with QA and product evidence workflows.

## 6. Positioning recommendation

### Current functional category

> AI coding agent and agentic work environment.

### Proposed adoption language

> A supervised team of agents that turns defined work into inspectable, reviewable outcomes.

### Supporting message

> Start with one expensive workflow. Delegate it safely. Measure the result. Scale only after the economics are visible.

This framing keeps human approval and evidence visible while broadening the market beyond code generation.

## 7. Highest-leverage experiments

1. **First Workflow Wizard** — route each participant to one bounded workflow based on role and recurring pain.
2. **Plan Decision Calculator** — recommend a plan category only after expected frequency, concurrency, and review burden are known.
3. **Seven-Day Build Week** — cohort-based activation with a real capacity limit rather than artificial scarcity.
4. **Outcome Receipt** — automatically summarize completed artifacts, time saved, review effort, quality score, and next recommended workflow.
5. **Upgrade Trigger Test** — compare generic limit messaging with evidence-based messaging tied to a user's completed work.

## 8. Risks

- Public pricing, plan availability, and limits can change quickly.
- Self-reported hours saved are vulnerable to optimism bias.
- Correlation between pilot participation and conversion does not establish incrementality.
- Revenue share is impossible to administer fairly without cohort IDs, baselines, exclusions, and a fixed attribution period.
- Broad non-developer positioning can create trust or safety concerns if human authority is not explicit.
- An independent project must not imply OpenAI endorsement.

## Official sources

- [ChatGPT plans](https://openai.com/chatgpt/pricing/)
- [ChatGPT Business pricing](https://openai.com/business/pricing/)
- [Codex rate card](https://help.openai.com/en/articles/20001106-codex-rate-card-2)
- [Managing credits and spend controls in ChatGPT Business](https://help.openai.com/en/articles/20001155)
- [GPT-5.6 model comparison](https://developers.openai.com/api/docs/models/compare)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/)
- [Codex is becoming a productivity tool for everyone](https://openai.com/index/codex-for-knowledge-work/)
- [How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)
