# Codex Adoption Lab

**Codex Adoption Lab** is an evidence-based go-to-market and adoption initiative for helping QA professionals, product managers, analysts, founders, and small technology teams turn Codex capabilities into completed workflows, accepted artifacts, and sustainable usage decisions.

This is an independent proposal and is not affiliated with or endorsed by OpenAI.

## Thesis

Codex is moving from a coding assistant toward a command center for parallel agents and broader knowledge work. The product capability is expanding faster than the average user's ability to understand:

1. what work to delegate;
2. how to achieve a first successful outcome;
3. which subscription or usage model fits that outcome;
4. how to measure the economic value of adoption.

The Lab focuses on that gap.

> The opportunity is not to explain more features. It is to help a user complete one valuable workflow, prove the result, and then select the right plan with confidence.

## Current evidence snapshot

The initial strategy is grounded in official OpenAI materials available in July 2026:

- Codex pricing moved from approximate per-message pricing to token-aligned usage on **April 2, 2026**, with the remaining existing Enterprise plans moved on **April 23, 2026**.
- Codex supports parallel agent work and can be supervised across app, CLI, IDE, cloud, and mobile experiences.
- More than 5 million people use Codex weekly, and knowledge workers represent about 20% of users.
- In May 2026, 70.2% of sampled individual users made at least one Codex request estimated to exceed one hour of human work.
- OpenAI launched its Partner Network in June 2026 to help organizations move from AI ambition to measurable outcomes.

See [`docs/01-market-audit.md`](docs/01-market-audit.md), [`docs/06-claim-evidence-matrix.md`](docs/06-claim-evidence-matrix.md), and [`docs/08-documentation-integrity.md`](docs/08-documentation-integrity.md) for sources, qualifications, review dates, and integrity controls.

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
Human acceptance or rejection
    ↓
Time, quality, and failure measurement
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
- [`docs/02-plf-launch-strategy.md`](docs/02-plf-launch-strategy.md) — internal educational launch and conversion sequence.
- [`docs/03-eight-week-pilot.md`](docs/03-eight-week-pilot.md) — bounded pilot scope, delivery plan, and acceptance criteria.
- [`docs/04-partnership-proposal.md`](docs/04-partnership-proposal.md) — proposed collaboration structure for OpenAI or an implementation partner.
- [`docs/05-measurement-framework.md`](docs/05-measurement-framework.md) — activation, retention, value, and revenue-attribution model.
- [`docs/06-claim-evidence-matrix.md`](docs/06-claim-evidence-matrix.md) — material claims, official sources, qualifiers, and machine-checkable review dates.
- [`docs/07-partner-entry-strategy.md`](docs/07-partner-entry-strategy.md) — proof-led co-delivery and direct Partner Network paths.
- [`docs/08-documentation-integrity.md`](docs/08-documentation-integrity.md) — link, freshness, workflow-security, and manual-fallback controls.

### Runnable pilot kit

- [`pilot/README.md`](pilot/README.md) — sequence, hard start gate, evidence requirements, and commercial gate.
- [`pilot/participant-screener.md`](pilot/participant-screener.md) — suitability and exclusion screening.
- [`pilot/participant-consent.md`](pilot/participant-consent.md) — consent, data, and publication boundaries.
- [`pilot/first-workflow-selector.md`](pilot/first-workflow-selector.md) — choose one safe, reviewable, repeatable workflow.
- [`pilot/baseline-form.md`](pilot/baseline-form.md) — frozen human-only baseline.
- [`pilot/context-pack.md`](pilot/context-pack.md) — source, requirement, unknown, and permission record.
- [`pilot/workflow-map.md`](pilot/workflow-map.md) — bounded QA/Product audit workflow and human gates.
- [`pilot/task-decomposition.md`](pilot/task-decomposition.md) — bounded agent tasks, dependencies, evidence, and budgets.
- [`pilot/safety-boundary.md`](pilot/safety-boundary.md) — authority, data, environment, and stop boundaries.
- [`pilot/acceptance-rubric.md`](pilot/acceptance-rubric.md) — stable accepted, partially accepted, and rejected criteria.
- [`pilot/outcome-receipt.md`](pilot/outcome-receipt.md) — auditable time, quality, failure, and economics summary.
- [`pilot/follow-up-form.md`](pilot/follow-up-form.md) — day-7 and day-30 retention follow-up.
- [`evidence/metric-dictionary.md`](evidence/metric-dictionary.md) — frozen measurement definitions.
- [`evidence/failure-register.md`](evidence/failure-register.md) — failure taxonomy and incident record.
- [`evidence/cases/CAL-001/case-record.md`](evidence/cases/CAL-001/case-record.md) — first real internal process-validation case and owner sign-off.
- [`examples/anonymized-qa-product-audit.md`](examples/anonymized-qa-product-audit.md) — synthetic worked example; not performance evidence.

## Operating principles

1. **Evidence before claims.** Separate confirmed facts, assumptions, experiments, and forecasts.
2. **Outcome before plan selection.** Recommend a plan category only after defining the workflow and expected usage.
3. **One segment, one transformation.** Avoid a generic launch for every profession at once.
4. **No artificial scarcity.** Any cohort window must be tied to real operating capacity.
5. **Human authority remains explicit.** Agents may investigate, draft, test, and propose; accountable humans approve consequential actions.
6. **Attribution must be agreed in advance.** Performance compensation requires a bounded cohort, baseline, tracking method, exclusions, and time window.
7. **Failures remain visible.** Rejected findings and negative time savings are part of the evidence.
8. **No baseline, no savings claim.** Missing pre-run measurement invalidates time and ROI reporting.
9. **Volatile claims expire.** Partner-facing facts require claim-level review dates and integrity checks.

## CAL-001 result

The first internal validation case inspected exact source state `a78a5c7fa05cdab877c73fe5aaab8007a3cb8a41`.

Final result:

- owner decision: `partially accepted`;
- weighted score on the audited state: `3.10 / 4.00`;
- no valid time-saved or ROI metric because the baseline was not frozen before the run;
- four confirmed process or documentation gaps;
- no safety or authority violation observed.

The case triggered corrections to pricing interpretation, claim traceability, pilot assets, participant consent, partner-entry strategy, and documentation-integrity controls.

## Immediate milestone

Complete the documentation-integrity gate, merge the corrected stack in order, then run four additional friendly participant workflows before external performance-based outreach.

The seed cohort does not claim attributable subscription or API revenue.

## Status

**Phase:** Pilot Kit v0.2, CAL-001 signed off, integrity controls in review  
**Delivery mode:** stacked draft pull requests  
**Next gate:** documentation-integrity validation, then four additional real seed cases.

## Primary official sources

- [ChatGPT pricing](https://chatgpt.com/pricing/)
- [ChatGPT Business pricing](https://openai.com/business/pricing/)
- [Codex rate card](https://help.openai.com/en/articles/20001106)
- [GPT-5.6](https://openai.com/index/gpt-5-6/)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/)
- [Codex is becoming a productivity tool for everyone](https://openai.com/index/codex-for-knowledge-work/)
- [How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)
- [Introducing the OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network/)
