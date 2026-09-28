# Codex market and pricing audit

**Source review date:** 2026-09-17

**Scope:** plan access and billing structure, historical adoption evidence, and Lab adoption hypotheses. This is not a current model-price catalogue.

Material factual claims are mapped in [`06-claim-evidence-matrix.md`](06-claim-evidence-matrix.md). Live pricing, availability, limits, and policies remain the source of truth.

## 1. Historical adoption evidence

OpenAI's June 2026 publications reported that:

- Codex had more than 5 million weekly active users;
- knowledge workers represented about 20% of users and were growing more than three times as fast as developers;
- in May 2026, 70.2% of sampled individual users made at least one Codex request estimated to exceed one hour of human work.

These are historical observations, not September user counts or Lab results. The task-duration estimate used an LLM judge and a random 0.1% sample of individual users. It is not a measurement of time saved. See claims `C-010` through `C-012`.

The Lab infers an opportunity to help people adopt broader workflows. Whether a guided first task improves paid conversion remains an experiment.

## 2. Current offer ladder

The public ChatGPT plan ladder currently includes:

| Plan | Codex role in the ladder | Primary adoption job |
|---|---|---|
| Free | Limited Codex access | Demonstrate that an agent can complete a real task |
| Go | Limited Codex access | Keep light users engaged before professional adoption |
| Plus | Expanded Codex usage | Establish a weekly professional workflow |
| Pro | Maximum Codex tasks, subject to limits | Support intensive, parallel, daily agent work |
| Business | Shared secure workspace, administration, analytics, budgeting, and Codex | Move from individual success to team deployment |
| Enterprise | Custom scale, controls, support, and commercial terms | Govern agentic work in large organizations |

The `Primary adoption job` column is a Lab interpretation, not official plan language. Public prices and local-currency offers can change by region and account. The live pricing page should remain the source of truth for exact personal-plan prices. See claim `C-001`.

### Business pricing

At this review, Business offers Standard and Premium seats. USD monthly equivalents are $20/$100 billed annually, or $25/$125 billed monthly. A workspace needs two seats in total; types can be mixed. Both include Codex, while API billing is separate. Regional pricing may differ.

Legacy Codex-only seats are restricted to eligible workspaces that added that seat type before June 24, 2026. See claims `C-002` through `C-004` and the [Business overview](https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/).

## 3. Billing structure at review

For credit-based workspaces, the current [ChatGPT rate card](https://help.openai.com/en/articles/11481834) meters Work and Codex by input, cached-input, and output tokens. Some Enterprise workspaces still use legacy rates until migration; the applicable agreement matters. See `C-019` and `C-020`.

The July migration summary has been removed because the redirected source does not support it as current guidance. The average-spend estimate remains in the source, but is omitted here because it cannot establish a participant budget. See the [review record](09-source-review-2026-09-17.md).

### Marketing consequence

Token alignment improves cost traceability, but it also increases cognitive load. A buyer must understand:

- included plan usage;
- credits after included limits;
- model mix;
- cached versus uncached input;
- cache reads versus cache creation where applicable;
- output-heavy tasks;
- parallel instances and automations.

This is economically rational infrastructure pricing, but it is not yet a simple adoption story for a first-time buyer. That conclusion is a Lab inference.

## 4. Cost measurement protocol

The static GPT-5.6 price table is retired. The [release page](https://openai.com/index/gpt-5-6/) now carries later price-change notices, so the July table cannot support a current budget. Old preview wording is also unsuitable for a current availability recommendation.

Before a participant run, record the actual model, account access, billing mode, applicable live rates, date, and budget in the [context pack](../pilot/context-pack.md). Check API availability separately from subscription access. Measure usage and human review effort for the run; account for retries and rejected outputs.

The Lab's decision unit is **cost per accepted completed workflow**. A model's token price alone cannot establish that result. Retired claim IDs `C-007` through `C-009` must not be reused as current guidance.

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

This is a Lab decision framework, not an official OpenAI plan recommendation.

#### Gap C — economic proof arrives too late

The first-session experience should help users capture:

- baseline human time;
- agent runtime;
- setup and review time;
- accepted output;
- rework;
- verified avoided direct cost where available;
- repeatability.

Without that measurement, an upgrade feels like buying more AI. With it, an upgrade may feel like funding a proven operating system. This remains a hypothesis to test.

#### Gap D — different professions require different entry stories

A developer, QA lead, product manager, analyst, and founder may use the same platform but do not buy the same transformation.

The initial Lab pilot therefore avoids a universal campaign and begins with QA and product evidence workflows. See claims `C-015` and `C-016`.

## 6. Positioning recommendation

### Current functional category

> AI coding agent and agentic work environment.

### Proposed adoption language

> A supervised team of agents that turns defined work into inspectable, reviewable outcomes.

### Supporting message

> Start with one expensive workflow. Delegate it safely. Measure the result. Scale only after the economics are visible.

This framing is a Lab proposal. It keeps human approval and evidence visible while broadening the market beyond code generation.

## 7. Highest-leverage experiments

1. **First Workflow Selector** — route each participant to one bounded workflow based on role and recurring pain.
2. **Plan Decision Calculator** — recommend a plan category only after expected frequency, concurrency, and review burden are known.
3. **Seven-Day Build Week** — cohort-based activation with a real capacity limit rather than artificial scarcity.
4. **Outcome Receipt** — summarize completed artifacts, time saved where a valid baseline exists, review effort, quality score, failures, and next recommended workflow.
5. **Upgrade Trigger Test** — compare generic limit messaging with evidence-based messaging tied to accepted work.

These are experiments, not proven conversion mechanisms.

## 8. Risks

- Public pricing, plan availability, and limits can change quickly.
- Self-reported hours saved are vulnerable to optimism bias.
- A missing pre-run baseline invalidates time-saved and ROI claims.
- Correlation between pilot participation and conversion does not establish incrementality.
- Revenue share is impossible to administer fairly without cohort IDs, baselines, exclusions, and a fixed attribution period.
- Broad non-developer positioning can create trust or safety concerns if human authority is not explicit.
- An independent project must not imply OpenAI endorsement.
- Direct Partner Network qualification may require delivery, customer, and co-sell evidence beyond an initial concept package.

## Official sources

- [ChatGPT plans](https://chatgpt.com/pricing/)
- [ChatGPT Business pricing](https://openai.com/business/pricing/)
- [What is ChatGPT Business?](https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/)
- [ChatGPT rate card, including Work and Codex](https://help.openai.com/en/articles/11481834)
- [GPT-5.6 release and subsequent price-change notices](https://openai.com/index/gpt-5-6/)
- [GPT-5.6 model comparison](https://developers.openai.com/api/docs/models/compare)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/)
- [Codex is becoming a productivity tool for everyone](https://openai.com/index/codex-for-knowledge-work/)
- [How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)
- [Introducing the OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network/)
- [OpenAI Partner Network](https://openai.com/business/partners/)
