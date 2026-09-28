# Your first verifiable AI-assisted task

[Русская версия](first-ai-work-task-ru.md) · [Back to the Lab](../README.md)

Start with one small task, one inspectable artifact, and a human decision. This is a self-guided exercise, not enrollment in a pilot. Use a tool you already have access to; there is no need to buy a subscription for this exercise.

## 1. Define what done means

Finish this sentence before using AI:

> This task is done when I have …, and I can check it by …

Choose something narrow: test scenarios for one API, an explanation of one reproducible bug, or a review of one document. Avoid a whole product audit as a first exercise.

## 2. Supply only safe, relevant context

Record the goal, source and version, allowed actions, acceptance checks, and unanswered questions. Use a public repository or synthetic material. Work materials require your organization's approved tools and access rules.

Do not share credentials, personal data, customer records, private code, or screenshots containing confidential information. Sanitizing a filename alone does not sanitize a file.

The [context-pack template](../pilot/context-pack.md) has the fuller version.

## 3. Try this small example

**Synthetic practice specification — no live API is involved:**

- `GET /demo/tasks` accepts an integer `page_size` from 1 through 100, inclusive.
- Omitting `page_size` uses 20.
- Out-of-range or non-integer values return HTTP 400.

Copy this prompt with the specification above:

```text
Using only this specification, draft six test scenarios:
page_size=1, page_size=100, omitted, page_size=0,
page_size=101, and page_size=abc.

For each, include the input, expected behavior, supporting requirement,
and what evidence would be needed to check an implementation.
Do not invent a response schema or claim that tests were executed.
Mark anything not specified as unknown.
```

Your artifact is a small test table. Check that both boundaries are allowed, omission selects 20, and the three invalid inputs expect 400. Response-body fields, success status, authentication, and implementation behavior remain unspecified.

**Accepting the test table is not evidence that an API passed these tests.** There is no running service in this exercise.

## 4. Review the result, not just the wording

Compare every expectation with the supplied specification. Ask what is supported, what is only proposed, and what remains untested. Save one concrete counterexample when an answer is wrong; change one substantial condition at a time when retrying.

For a real task, retain the source version, relevant artifact or diff, and actual test output where available. A command completing successfully does not by itself establish that the original requirement was met.

Use the [acceptance rubric](../pilot/acceptance-rubric.md) for a fuller review. Record one decision: `accepted`, `partially accepted`, or `rejected`, with a reason and the next correction.

## 5. Keep measurement honest

The Lab's [CAL-001 record](../evidence/cases/CAL-001/case-record.md) is one internal documentation audit of a pinned historical revision. Its owner marked it **partially accepted**. A human-only baseline was not frozen before the run, so it does not establish time saved or ROI. It is not an external participant success story.

For a measured pilot, freeze a comparable baseline before work begins and include context preparation, review, and rework in assisted time. Without comparable measurements, leave savings unknown. The [pilot start gate](../pilot/README.md), including screening and consent, still applies; this exercise does not replace it.

## Next step

Keep the reviewed artifact and write down what you can now do independently. To propose a real task, use the repository's **Propose one verifiable workflow** issue template with a public or synthetic example, expected result, and human reviewer.

An issue is public and is only a proposal. It is not a booking, an access grant, or consent to publish a case study. Do not post confidential inputs or assume a response deadline.

---

English adaptation of the [Russian guide](first-ai-work-task-ru.md), with a synthetic practice exercise added. Independent project; not affiliated with or endorsed by OpenAI. Neither this exercise nor the synthetic worked examples establish performance or customer outcomes.
