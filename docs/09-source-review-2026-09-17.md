# Source review — 2026-09-17

## Why this review was necessary

[Documentation integrity run 34959781647](https://github.com/safal207/Codex-Adoption-Lab/actions/runs/34959781647) failed because 11 official claims had passed their review deadlines. The checker tests, internal links, and external-material guardrails passed. This was a stale-evidence failure, not a reason to relax the gate.

This review opens the source pages, corrects current guidance, and removes unsupported or unnecessary claims. The checker, expiry rules, and workflow security model are unchanged.

## Source observations and decisions

| Source accessed on 2026-09-17 | Observation | Repository decision |
|---|---|---|
| [ChatGPT pricing](https://chatgpt.com/pricing/) | The current access ladder supports the revised C-001. | Remove the old multiplier wording; do not make a plan recommendation from a cached limit. |
| [Business overview](https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/) | Seat options and the minimum-seat rule changed. | Update C-002–C-004 and the market audit together. |
| [Current rate card](https://help.openai.com/en/articles/11481834) | The former `/20001106` source redirects here; legacy Enterprise rates remain documented. | Withdraw C-005/C-006 and the unsupported average-spend estimate. Add narrower current claims C-019/C-020. |
| [GPT-5.6 release](https://openai.com/index/gpt-5-6/) | July 30 and August 21 update notices change prices after the old snapshot; the article describes general availability. | Retire the July price table and preview-oriented guidance (C-007–C-009). Do not substitute an unverified new price table. |
| [June 2 adoption report](https://openai.com/index/codex-for-knowledge-work/) and [June 25 work report](https://openai.com/index/how-agents-are-transforming-work/) | The quoted historical figures remain present. | Date C-010–C-012 explicitly; retain their existing October review deadline. These are not current counts or measured Lab savings. |
| [Partner Network announcement](https://openai.com/index/introducing-openai-partner-network/) and [program page](https://openai.com/business/partners/) | The scoped program description remains supported. | Refresh C-013/C-014; preserve the Lab's independent status and lack of external delivery proof. |

The [active matrix](06-claim-evidence-matrix.md) records proposed review deadlines. The [pre-review revision](https://github.com/safal207/Codex-Adoption-Lab/tree/98a9c273458f6550207e4536648deedfb16c3ff9) preserves old values and dates. Retired IDs are not evidence for new recommendations.

## Review boundaries

- This is a Codex-assisted documentation review submitted for maintainer approval, not a claim of completed human sign-off.
- A source access date records when its contents were inspected. It is not a publication date, account-specific quote, or promise that the page will remain unchanged.
- URL reachability alone cannot validate a claim. Redirects and source contents must be inspected.
- Model pricing and eligibility must be checked for the actual account before a cost recommendation. No subscription purchase or partner enrollment was performed.
- CAL-001 remains an internal, partially accepted process-validation case. No new participant outcome, time saving, ROI, or partner status is claimed.
- Weekly checks will fail again when active claims expire unless the next source review happens. This is intentional.
