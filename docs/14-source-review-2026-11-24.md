# November 24, 2026 — source inspection and proposed claim renewal

Status: **ASSISTANT REVIEW ONLY / HOLD**. Inspection date 2026-11-24 (UTC date at inspection may still be November 23; no active verification date is assigned). Existing PR #13, prior head 088336a0f8cd5811bcfb793d774d0b6f7e8f9d4d. This packet supersedes the October 19 proposals for review purposes only. It does not promote them to the active matrix, attest human verification, or authorize merge.

Main scheduled failure: [run 45233314775](https://github.com/safal207/Codex-Adoption-Lab/actions/runs/45233314775), 11 expired findings, 9 passed. All 11 active official IDs inspected below. Sources are live official pages retrieved through assistant web inspection, not the scheduled HTTP probe. Retrieval is not human verification. Earlier verification records and retired IDs remain intact.

## Source index

- S1: [Codex pricing / ChatGPT Learn](https://learn.chatgpt.com/docs/pricing), sections Pricing, Pricing options and API Key. Original developers.openai.com/codex/pricing/ redirects here.
- S2: [Business overview](https://help.openai.com/en/articles/8792828-chatgpt-business-overview), seat table, Overview, FAQ and comparison with API.
- S3: [Business signup](https://help.openai.com/en/articles/8980713-sign-up-for-chatgpt-business), Overview and Choose paid seat capacity.
- S4: [Codex knowledge work announcement](https://openai.com/index/codex-for-knowledge-work/), June 2, 2026.
- S5: [How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/), June 25, 2026, first finding, longer-horizon section and footnotes 1–2.
- S6: [Partner Network announcement](https://openai.com/index/introducing-openai-partner-network/), June 14, 2026, program description and tier section.
- S7: [Partner Network](https://openai.com/business/partners/), outcomes and enrollment sections.
- S8: [Credit-based rate card](https://help.openai.com/en/articles/11481834), Overview, ChatGPT Work and Codex, and Legacy rates.

## Proposed active claim wording (not applied)

| ID | Proposed wording / disposition | Source and human verification target |
|---|---|---|
| C-001 | Codex is included across Free, Go, Plus, Pro, Business, Edu and Enterprise. Desktop Free/Go access depends on rollout; usage and access vary by plan, model and surface. Do not promise a fixed task allowance. | S1: plan inclusion and Free/Go rollout notes; verify account-specific limits. |
| C-002 | Business Standard costs USD 20 per seat/month on annual billing or 25 monthly; Premium costs 100 or 125 respectively. The current signup guide and overview permit one paid Standard or Premium seat for a new workspace. Local price and checkout requirements may differ; confirm at checkout. | S2/S3: seat table and one-seat statements. S1 still states 2+ users in its Business pricing footnote; record the conflict, prioritize current signup-specific guidance, do not guarantee checkout eligibility. |
| C-003 | Both Standard and Premium Business seats cover ChatGPT, Work and Codex; Premium provides greater usage capacity. API billing is independent. | S2: table and comparison with API. |
| C-004 | Only eligible Business workspaces that added the legacy Codex-only seat type before June 24, 2026 can retain access to that type. | S2/S3: legacy seat note. |
| C-010 | OpenAI reported over five million weekly active Codex users on June 2, 2026; not a current user count. | S4: dated announcement. |
| C-011 | The same June 2 report estimated knowledge workers at roughly one fifth of users; their growth rate was more than triple developers' growth rate. | S4: preserve date and approximation. |
| C-012 | In May 2026, 70.2% of sampled individual users submitted at least one request with an estimated human task horizon above one hour. Estimates use an LLM judge on transcripts and queries from a random 0.1% sample; directional rather than exact, not measured time savings or completion rates. | S5: first finding and footnotes 1–2. |
| C-013 | On June 14, 2026 OpenAI announced a partner program intended to help organizations adopt and deploy AI solutions, including workflow integration and change management. | S6: dated launch and program purpose. |
| C-014 | Partner progression through Select, Advanced and Elite considers commercial results, technical strength, joint selling and deployment track record. The public program also seeks sector knowledge, customer relationships and delivery capability; enrollment is consideration, not acceptance. No Lab eligibility or affiliation is implied. | S6: tiers; S7: outcomes and enrollment. |
| C-019 | For applicable credit-based flexible workspaces, Work/Codex Standard-mode charges use credits per million input, cached input and output tokens. The rate card specifies eligible Business standard/legacy Codex seat users and credit-based Enterprise/Edu and additional named workspace categories. Included limits, seat-specific treatment, speed multipliers, legacy rates and USD agreements need separate checks; API pricing is separate. Do not infer Premium-specific rates from a section naming standard seats. | S8: Work/Codex applicability, limits and Legacy rates; S2 for Premium flexible credits. |
| C-020 | Some Enterprise workspaces remain on legacy Codex rates until migrated; the workspace agreement determines applicable credit or USD rates. | S8: Legacy Codex rate card and final applicability guidance. |

## Maintainer checklist

- [ ] Personally open S1 and verify C-001 and its limits.
- [ ] Open S2 and S3, compare S1's older minimum, verify C-002/C-003/C-004; retain conflict caveat or hold C-002.
- [ ] Open S4 and confirm C-010/C-011 as historical.
- [ ] Open S5 including footnotes and confirm C-012 with methodology.
- [ ] Open S6/S7 and confirm C-013/C-014 without claiming partnership.
- [ ] Open S8 and confirm C-019/C-020 including contract-specific exceptions.
- [ ] Record actual human reviewer, date, scope and disposition for each ID. Renew only verified rows using existing cadence; reconcile downstream documents, including Business minimum-seat examples. Do not renew remaining claims or silently retire them.
- [ ] Run Documentation Integrity on exact resulting head. An expired-claim failure is expected until the authorized renewal is applied. Do not weaken checker, dates or tests to obtain green.

No merge, publication, partner application, or source attestation is included.

## Subsequent owner attestation — November 24 Moscow time (November 23 UTC)

The owner, Aleksey Safonov, explicitly stated in the task conversation:

> Я лично проверил все 11 утверждений и официальные источники из ноябрьского отчёта Codex Adoption Lab. Подтверждаю их актуализацию с сохранением оговорок. Обнови активную матрицу и проверь CI PR #13. Не мержи.

Scope: C-001, C-002, C-003, C-004, C-010, C-011, C-012, C-013, C-014, C-019, C-020. The owner reports personally verifying the official sources in this packet and approves updating the active matrix with qualifiers retained. This is a recorded human attestation, not independent evidence of browsing activity, not a GitHub APPROVED review and explicitly not merge authorization. The initial assistant-only section above is historical. UTC verification date: 2026-11-23. Weekly renewal through November 30 (C-001/C-002/C-019); fortnightly through December 7 (C-014); monthly or conservative 30-day historical recheck through December 23 (remaining seven claims). The before-use rules remain in effect. Business source conflict and actual-checkout caveat are retained in the active matrix; no claim of universal one-seat eligibility. No retired or non-official claim renewed. CI remains independently required.
