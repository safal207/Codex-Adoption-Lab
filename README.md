# Codex Adoption Lab

**Codex Adoption Lab** is an evidence-based go-to-market and adoption initiative for helping QA professionals, product managers, analysts, founders, and small technology teams turn Codex capabilities into completed workflows, saved time, and sustainable paid usage.

This is an independent proposal and is not affiliated with or endorsed by OpenAI.

## Thesis

Codex is moving from a coding assistant toward a command center for parallel agents and broader knowledge work. The product capability is expanding faster than the average user's ability to understand:

1. what work to delegate;
2. how to achieve a first successful outcome;
3. which subscription or usage model fits that outcome;
4. how to measure the economic value of adoption.

The Lab focuses on that gap.

> The marketing opportunity is not to explain more features. It is to help a user complete one valuable workflow, prove the result, and then select the right plan with confidence.

## Current evidence snapshot

The initial strategy is grounded in official OpenAI materials available in July 2026:

- Codex pricing moved from approximate per-message pricing to token-aligned usage on **April 2, 2026**, with the remaining existing Enterprise plans moved on **April 23, 2026**.
- Codex supports parallel agent work in its desktop app and can be supervised across app, CLI, IDE, cloud, and mobile experiences.
- More than 5 million people use Codex weekly, and knowledge workers represent a growing share of usage.
- In May 2026, more than 70% of users asked Codex to perform a task estimated to take a human more than one hour.
- OpenAI launched its Partner Network in June 2026 to help organizations move from AI ambition to measurable outcomes.

See [`docs/01-market-audit.md`](docs/01-market-audit.md) for sources, qualifications, and current constraints.

## Target segments

The first pilot is intentionally narrow:

- QA engineers and QA leads;
- product and system analysts;
- product managers;
- founders and small technical teams.

These groups share a useful adoption pattern: they have real, repeatable, evidence-heavy workflows but often lack a clear first agentic operating model.

## Core adoption loop

```text
Real workflow
    ↓
Guided first delegation
    ↓
Finished artifact with evidence
    ↓
Time and quality measurement
    ↓
Repeat usage
    ↓
Plan or API decision based on economics
```

## Proposed first workflow

**Codex for QA and Product Audit**

```text
Product or repository
    ↓
Requirements and journey mapping
    ↓
Risk-based test model
    ↓
API / UI / workflow investigation
    ↓
Evidence-backed findings
    ↓
Prioritized product backlog
    ↓
Management-ready report
```

The workflow is designed to produce inspectable artifacts rather than impressive but unverifiable claims.

## Repository map

### Strategy

- [`docs/01-market-audit.md`](docs/01-market-audit.md) — current product, pricing, adoption, and messaging audit.
- [`docs/02-plf-launch-strategy.md`](docs/02-plf-launch-strategy.md) — Product Launch Formula-inspired education and conversion sequence.
- [`docs/03-eight-week-pilot.md`](docs/03-eight-week-pilot.md) — bounded pilot scope, delivery plan, and acceptance criteria.
- [`docs/04-partnership-proposal.md`](docs/04-partnership-proposal.md) — proposed collaboration structure for OpenAI or an implementation partner.
- [`docs/05-measurement-framework.md`](docs/05-measurement-framework.md) — activation, retention, value, and revenue-attribution model.

### Runnable pilot kit

- [`pilot/README.md`](pilot/README.md) — sequence, evidence requirements, statuses, and commercial gate.
- [`pilot/participant-screener.md`](pilot/participant-screener.md) — suitability and exclusion screening.
- [`pilot/baseline-form.md`](pilot/baseline-form.md) — frozen human-only baseline.
- [`pilot/workflow-map.md`](pilot/workflow-map.md) — bounded QA/Product audit workflow and human gates.
- [`pilot/safety-boundary.md`](pilot/safety-boundary.md) — authority, data, environment, and stop boundaries.
- [`pilot/acceptance-rubric.md`](pilot/acceptance-rubric.md) — stable accepted, partially accepted, and rejected criteria.
- [`pilot/outcome-receipt.md`](pilot/outcome-receipt.md) — auditable time, quality, failure, and economics summary.
- [`pilot/follow-up-form.md`](pilot/follow-up-form.md) — day-7 and day-30 retention follow-up.
- [`evidence/metric-dictionary.md`](evidence/metric-dictionary.md) — frozen measurement definitions.
- [`evidence/failure-register.md`](evidence/failure-register.md) — failure taxonomy and incident record.
- [`examples/anonymized-qa-product-audit.md`](examples/anonymized-qa-product-audit.md) — synthetic worked example; not performance evidence.

## Operating principles

1. **Evidence before claims.** Separate confirmed facts, assumptions, experiments, and forecasts.
2. **Outcome before plan selection.** Recommend a subscription only after defining the workflow and expected usage.
3. **One segment, one transformation.** Avoid a generic launch for every profession at once.
4. **No artificial scarcity.** Any launch window must be tied to real cohort capacity or live support.
5. **Human authority remains explicit.** Agents may investigate, draft, test, and propose; accountable humans approve consequential actions.
6. **Attribution must be agreed in advance.** Performance compensation requires a bounded cohort, baseline, tracking method, exclusions, and time window.
7. **Failures remain visible.** Rejected findings and negative time savings are part of the evidence.

## Immediate milestone

Run the templates with **5 friendly participants** before external performance-based outreach and measure:

- first completed workflow;
- time to first value;
- net human time saved after setup, review, and rework;
- artifact quality and acceptance;
- false positives, omissions, and boundary incidents;
- repeat usage within seven and thirty days;
- plan-selection confidence.

The seed cohort does not claim attributable subscription or API revenue.

## Status

**Phase:** pilot kit v0.1 ready for review  
**Delivery mode:** stacked draft pull requests  
**Next gate:** run one real internal case, revise the kit, then recruit four additional friendly participants.

## Primary official sources

- [Codex rate card](https://help.openai.com/en/articles/20001106-codex-rate-card-2)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/)
- [Codex is becoming a productivity tool for everyone](https://openai.com/index/codex-for-knowledge-work/)
- [How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)
- [Introducing the OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network/)