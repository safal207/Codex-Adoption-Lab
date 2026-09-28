# Codex Adoption Lab

**One Codex task → one inspectable artifact → a human decision.**

An open collection of guides, templates, and review protocols for QA engineers, analysts, product managers, and small technical teams. Start with a bounded task, check the result against its sources, and record what was accepted, rejected, or left unknown.

This is a documentation and pilot kit, not an automated verifier or a hosted service. Independent project; not affiliated with or endorsed by OpenAI.

## Start here

- **Try one task:** [English guide](external/first-ai-work-task-en.md) · [Русская инструкция](external/first-ai-work-task-ru.md). The English guide includes a synthetic practice specification; no private code or live service is needed for that exercise.
- **See the output format:** [Worked QA/Product audit](examples/anonymized-qa-product-audit.md). This example is synthetic, not evidence of performance or customer results.
- **Propose your task:** [Open a workflow proposal](https://github.com/safal207/Codex-Adoption-Lab/issues/new?template=propose-workflow.md) using a public or synthetic example, a source version, and acceptance checks. [Preview the template](.github/ISSUE_TEMPLATE/propose-workflow.md).

**Evidence boundary:** [CAL-001](evidence/cases/CAL-001/case-record.md) is one real internal audit, marked **partially accepted**. It has no valid time-saved or ROI measurement. External participant outcomes are not yet demonstrated.

**Keep private material out of issues.** Do not post credentials, personal data, customer records, private code, or confidential screenshots. An issue is a proposal, not enrollment, a response-time promise, a system-access grant, or consent to publish a case study. The [formal pilot start gate](pilot/README.md) still applies.

## Thesis

The Lab's working hypothesis is that completing one bounded, human-reviewed workflow is a better starting point for adoption than explaining more features. The questions are practical:

1. What work can be delegated safely?
2. What artifact would count as a useful result?
3. How will a human check it?
4. What evidence is needed before making a usage or budget decision?

This hypothesis requires real participant measurement; the kit does not establish it as proven.

## Evidence and scope

The [September 28 partial source review](docs/10-source-review-2026-09-28.md) records the claims rechecked and the remaining approval boundaries. The [September 17 review](docs/09-source-review-2026-09-17.md) records earlier corrections and withdrawn claims. Source access, automated freshness checks, external HTTP reachability, and human approval are separate checks.

The [market audit](docs/01-market-audit.md) separates dated product information from historical adoption research. Pricing and access must be checked for the participant's actual account before a recommendation. Consult the [claim–evidence matrix](docs/06-claim-evidence-matrix.md) and [documentation-integrity rules](docs/08-documentation-integrity.md), rather than treating an old price or model table as current.

## Target segments

The first pilot is intentionally narrow:

- QA engineers and QA leads;
- product and system analysts;
- product managers;
- founders and small technical teams.

The initial focus is repeatable work with explicit sources, reviewable artifacts, and a human able to decide whether the result meets the task.

## Core adoption loop

```text
One bounded workflow and pinned inputs
    ↓
Explicit permissions and acceptance checks
    ↓
AI-assisted artifact with supporting evidence
    ↓
Human acceptance, partial acceptance, or rejection
    ↓
Record limitations, review effort, and next correction
    ↓
Repeat or stop based on the observed result
```

For measured pilots, freeze the human-only baseline before the run. Plan or API decisions come after account-specific access, usage, and budget checks—not from an unmeasured promise of savings.

## Proposed first workflow

**Codex for QA and Product Audit**

```text
One product journey, endpoint, or document
    ↓
Requirements and unknowns
    ↓
Risk-based checks
    ↓
Bounded investigation
    ↓
Evidence-backed findings and untested conditions
    ↓
Prioritized corrections for human review
```

A useful first artifact might be six API test scenarios with source references. Drafted scenarios are not executed tests; a finished report is not automatic acceptance.

## Repository map

### Strategy

- [`docs/01-market-audit.md`](docs/01-market-audit.md) — dated product and billing snapshot, historical adoption evidence, and messaging hypotheses.
- [`docs/02-plf-launch-strategy.md`](docs/02-plf-launch-strategy.md) — internal educational launch and conversion sequence.
- [`docs/03-eight-week-pilot.md`](docs/03-eight-week-pilot.md) — bounded pilot scope, delivery plan, and acceptance criteria.
- [`docs/04-partnership-proposal.md`](docs/04-partnership-proposal.md) — proposed collaboration structure; not an agreed OpenAI partnership.
- [`docs/05-measurement-framework.md`](docs/05-measurement-framework.md) — activation, retention, value, and revenue-attribution model.
- [`docs/06-claim-evidence-matrix.md`](docs/06-claim-evidence-matrix.md) — material claims, sources, qualifiers, and review dates.
- [`docs/07-partner-entry-strategy.md`](docs/07-partner-entry-strategy.md) — proof-led co-delivery and direct Partner Network paths.
- [`docs/08-documentation-integrity.md`](docs/08-documentation-integrity.md) — link, freshness, workflow-security, and manual-fallback controls.
- [`docs/09-source-review-2026-09-17.md`](docs/09-source-review-2026-09-17.md) — source changes, retired claims, and review limitations.
- [`docs/10-source-review-2026-09-28.md`](docs/10-source-review-2026-09-28.md) — latest scoped review and public-entry preparation.

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

The case triggered corrections to pricing interpretation, claim traceability, pilot assets, participant consent, partner-entry strategy, and documentation-integrity controls. These are findings about the recorded historical state, not proof that every gap remains present today.

## Immediate milestone

Review the source corrections and keep the documentation-integrity gate current. Then run four additional friendly participant workflows before external performance-based outreach. Freeze each baseline before the run and publish only consented evidence.

The seed cohort does not claim attributable subscription or API revenue.

## Status

**Phase:** Pilot Kit v0.2 with CAL-001 signed off; documentation-integrity controls are implemented.

**Evidence maturity:** one internal case; additional seed cases remain a milestone. This is an open laboratory, not a validated service at scale.

**Validation:** inspect the [latest documentation-integrity runs](https://github.com/safal207/Codex-Adoption-Lab/actions/workflows/docs-integrity.yml) and the source-review records. A green PR check alone does not mean external URLs were probed or a maintainer approved the sources.

**Next gate:** maintainer source review, documentation validation, and a check of the three Start here paths in the default branch before directing new traffic.

## Primary official sources

- [ChatGPT pricing](https://chatgpt.com/pricing/)
- [ChatGPT Business pricing](https://openai.com/business/pricing/)
- [ChatGPT rate card, including Work and Codex](https://help.openai.com/en/articles/11481834)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/)
- [Codex is becoming a productivity tool for everyone](https://openai.com/index/codex-for-knowledge-work/)
- [How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)
- [Introducing the OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network/)
