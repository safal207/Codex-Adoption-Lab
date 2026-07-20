# Claim–evidence matrix

**Snapshot date:** 2026-07-21  
**Purpose:** map each material public claim to a specific official source, classification, and freshness rule.

This file is part of the evidence contract. A source list at the end of a document is not sufficient when a reader cannot determine which source supports which claim.

## Classifications

- `official fact` — stated by OpenAI in an official product, help, pricing, or announcement page.
- `Lab inference` — reasoned interpretation based on official facts; not an OpenAI claim.
- `Lab proposal` — proposed strategy, experiment, metric, or commercial term.
- `illustrative calculation` — example mathematics, not observed performance.

## Matrix

| Claim ID | Material claim | Classification | Official evidence | Published / updated | Accessed | Freshness rule |
|---|---|---|---|---|---|---|
| C-001 | Free and Go currently provide limited Codex access; Plus expands Codex usage; Pro provides maximum Codex tasks and 5x or 20x more usage. | official fact | https://chatgpt.com/pricing/ | live pricing page | 2026-07-21 | Recheck before every external use and at least weekly during a launch. |
| C-002 | ChatGPT Business is advertised at $20/user/month billed annually or $25 billed monthly, with a two-seat minimum for standard ChatGPT seats. | official fact | https://openai.com/business/pricing/ | live pricing page | 2026-07-21 | Recheck before every external use. |
| C-003 | Standard Business seats include ChatGPT and Codex; API usage is separate. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ | help article, updated dynamically | 2026-07-21 | Recheck monthly and before a proposal. |
| C-004 | Starting June 24, 2026, a new Business workspace or one without a prior Codex seat cannot add its first usage-based Codex-only seat; eligible existing workspaces may continue. | official fact | https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/ and https://openai.com/index/codex-flexible-pricing-for-teams/ | 2026-06-24 update | 2026-07-21 | Recheck monthly and before any seat recommendation. |
| C-005 | Codex pricing moved from approximate per-message pricing to API-token-aligned usage on April 2, 2026 for Plus, Pro, Business and new Enterprise plans. | official fact | https://help.openai.com/en/articles/20001106 | 2026-04-02 | 2026-07-21 | Recheck if rate card is updated. |
| C-006 | Remaining existing Enterprise plans, including Edu, Health, Gov and ChatGPT for Teachers, moved to the updated approach on April 23, 2026. | official fact | https://help.openai.com/en/articles/20001106 | 2026-04-23 | 2026-07-21 | Recheck if rate card is updated. |
| C-007 | GPT-5.6 published API prices per 1M tokens are Sol $5 input/$30 output, Terra $2.50/$15, and Luna $1/$6. | official fact | https://openai.com/index/gpt-5-6/ and https://help.openai.com/en/articles/20001325-a-preview-of-gpt-5-6-sol-terra-and-luna/ | 2026-07 | 2026-07-21 | Recheck before any cost model. |
| C-008 | GPT-5.6 cache writes are billed at 1.25x uncached input and cache reads receive a 90% input discount. | official fact | https://openai.com/index/gpt-5-6/ | 2026-07 | 2026-07-21 | Recheck before any cost model. |
| C-009 | GPT-5.6 API availability must be described with its current preview or access status, separately from ChatGPT plan availability. | official fact / documentation rule | https://help.openai.com/en/articles/20001325-a-preview-of-gpt-5-6-sol-terra-and-luna/ and https://chatgpt.com/pricing/ | live | 2026-07-21 | Recheck before every external use. |
| C-010 | Codex has more than 5 million weekly active users. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-07-21 | Recheck quarterly or when newer adoption data appears. |
| C-011 | Knowledge workers represent about 20% of Codex users and are growing more than three times as fast as developers. | official fact | https://openai.com/index/codex-for-knowledge-work/ | 2026-06-02 | 2026-07-21 | Recheck quarterly or when newer adoption data appears. |
| C-012 | In May 2026, 70.2% of sampled individual users made at least one Codex request estimated to exceed one hour of human work. | official fact with methodology limitation | https://openai.com/index/how-agents-are-transforming-work/ | 2026-06/07 | 2026-07-21 | Preserve the words “sampled,” “estimated,” and the month. |
| C-013 | OpenAI launched the Partner Network to help organizations identify use cases, redesign workflows, integrate systems, drive adoption, and create measurable impact. | official fact | https://openai.com/index/introducing-openai-partner-network/ | 2026-06-14 | 2026-07-21 | Recheck before partner outreach. |
| C-014 | The Partner Network currently emphasizes partner sales performance, technical capability, co-sell engagement, deployment experience, industry expertise, delivery capacity, and customer relationships. | official fact | https://openai.com/index/introducing-openai-partner-network/ and https://openai.com/business/partners/ | live / 2026-06-14 | 2026-07-21 | Recheck before enrollment or qualification claims. |
| C-015 | Helping a user complete one accepted workflow before recommending a plan may improve activation and plan confidence. | Lab hypothesis | Supported directionally by C-013; requires experiment | n/a | 2026-07-21 | Never state as proven until measured. |
| C-016 | The QA/Product segment is an attractive initial wedge because its work is evidence-heavy, reviewable, and repeatable. | Lab inference | Internal workflow analysis; not an OpenAI claim | n/a | 2026-07-21 | Validate through interviews and seed cases. |
| C-017 | A seven-day Build Week and three-event education sequence can improve activation, retention, or conversion. | Lab proposal | `docs/02-plf-launch-strategy.md` | n/a | 2026-07-21 | Requires controlled measurement; do not claim causality in advance. |
| C-018 | A 5–10% revenue share could be a negotiation option. | Lab proposal | `docs/04-partnership-proposal.md` | n/a | 2026-07-21 | Not an OpenAI term or market standard; use only after attribution and procurement review. |

## Rules for downstream documents

1. Reference the claim ID next to each material external claim where practical.
2. Preserve qualifiers such as `estimated`, `sampled`, `preview`, `about`, and exact dates.
3. Never convert a Lab inference into an official fact.
4. When a live pricing or help page changes, update this matrix before updating derived documents.
5. Record old values in version history rather than silently rewriting historical evidence.
6. External one-pagers should include only claims whose freshness check passed within the required window.

## Review log

| Version | Date | Reviewer | Change |
|---|---|---|---|
| 0.1 | 2026-07-21 | CAL-001 facilitator review | Initial material-claim mapping and freshness rules |
