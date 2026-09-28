# Source review and public entry preparation — 2026-09-28

**Review date:** 2026-09-28 (UTC). **Approval:** assistant-assisted source review; maintainer sign-off pending in draft PR #12.

This continues the existing [September 17 review](09-source-review-2026-09-17.md), rather than creating a competing correction stack. The starting PR head was `6d6e58c70be4bd806b2f4da4011a06d0099b3476`; its base was `98a9c273458f6550207e4536648deedfb16c3ff9`.

## What was actually rechecked

The following official pages were opened and their relevant contents inspected. A successful browser-backed content read is not an HTTP reachability verdict from GitHub Actions.

| Claims | Source inspected | Observation and decision | Proposed Review by |
|---|---|---|---|
| C-001 | [ChatGPT pricing](https://chatgpt.com/pricing/) | The bounded Free/Go, Plus, and Pro Codex access description remains supported. No fixed task allowance or old multiplier is restored. | 2026-10-05 |
| C-002 | [Business overview](https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/) | The two seat-price pairs and combined two-seat minimum remain supported. Preserve currency and regional qualifications. | 2026-10-05 |
| C-003, C-004 | [Business overview](https://help.openai.com/en/articles/8792828-what-is-chatgpt-team/) | Included access, separate API billing, and the legacy-seat eligibility boundary remain supported. | 2026-10-28 |
| C-019 | [Credit-based rate card](https://help.openai.com/en/articles/11481834) | Work/Codex use input, cached-input, and output token metering. Explicitly limit this claim to the credit-based Business/Enterprise/Edu rate card; it is not a universal API or subscription price. | 2026-10-05 |
| C-020 | [Credit-based rate card](https://help.openai.com/en/articles/11481834) | The legacy Enterprise exception remains; the customer's agreement determines applicable rates. | 2026-10-28 |
| C-013 | [Partner Network announcement](https://openai.com/index/introducing-openai-partner-network/) | The dated program purpose remains supported. This does not establish any Lab affiliation. | 2026-10-28 |
| C-014 | [Announcement](https://openai.com/index/introducing-openai-partner-network/) and [program page](https://openai.com/business/partners/) | The capability and delivery expectations remain supported. This is not an eligibility decision or evidence that the Lab qualifies. | 2026-10-12 |

The [matrix](06-claim-evidence-matrix.md) contains the proposed access dates and deadlines. Weekly, monthly, and fortnightly windows follow the existing rules; before-use review requirements still apply. Dynamic page update labels are not converted into invented publication dates.

**Not rechecked or revived:** C-010–C-012 retain their September 17 access dates, historical framing, and October 19 deadlines. C-005–C-009 remain explicitly retired by the existing PR. Their original statements and expired dates remain in the immutable pre-review matrix. This pass does not claim those five statements have been validated, nor does it add a new model-price table.

## Public entry changes

The README now starts with one bounded outcome and three paths: begin a task, inspect the synthetic example, or propose a public/synthetic workflow. The English guide includes a small synthetic specification that can be reviewed without private data or a live service. The Russian guide remains available.

The bilingual issue template asks for a pinned source, acceptance checks, boundaries, a human reviewer, and a baseline status. It warns that issues are public and must not contain secrets, personal data, or confidential work materials. Checkboxes are a self-check, not an automated data-loss-prevention mechanism. Submission does not grant access, enroll a participant, guarantee a response, or authorize publication of a case study.

## Gates and non-claims

- The checker, expiry policy, workflow permissions, and trusted-checker separation are unchanged.
- PR checks validate documentation, freshness metadata, and the existing external-material patterns. A green PR check is not approval of source truth by a human.
- The PR workflow does **not** probe external HTTP URLs. Scheduled or manually dispatched checks perform that separate probe. Existing `BLOCKED`/403 observations are not cleared by opening a source in a browser; no fresh external HTTP result is claimed here.
- Maintainer review of the corrected claims and proposed dates is still required before merge or external use. A manual source review does not rewrite an HTTP result as `PASS`.
- CAL-001 remains one internal, partially accepted case with no valid time-saved or ROI measurement. Synthetic exercises are not participant evidence.
- No load test, external participant validation, production deployment, partner enrollment, plan purchase, or social-media publication is included.

After maintainer review and merge, check the three README paths in the default branch. In particular, verify that GitHub renders the new issue template before directing traffic to it. Then invite a bounded first group; do not market this documentation kit as a finished service with guaranteed outcomes.
