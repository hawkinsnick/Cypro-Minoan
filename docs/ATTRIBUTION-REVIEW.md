# Attribution review

All six comparisons: five reassessments have an indirect Olivier side; one is an internal Valério inconsistency. Direct consultation and independence are separate questions.

Existing source consultation receipts and limits are inherited exactly from the referenced native packets. This pass inspects those packets, not the underlying publications afresh. No exhaustive literature search, new autopsy or independent review is claimed.

The complete selections below name the finite native collections reviewed. Other repository records and the broader literature are outside this checkpoint. Case counts are review tasks, not inscriptions, independent witnesses or fully attributed alternative pairs.

| Complete native selection | Rows |
|---|---:|
| `research/source-reconciliation.json/comparisons` | 6 |

Use the case query to read the finding together with the complete native evidence, including any named author/publication, source locator, inspection state, qualification and source dependence. Missing metadata stays missing; a source ID alone is not proof of direct consultation.

```sh
python scripts/attribution_review.py --check
python scripts/attribution_review.py --case 'CMOCC-0026-VALERIO2016-source-sequence-2-comparison'
python scripts/evidence_query.py --list attribution-review
```

| Review ID | Type | Finding | Remaining work |
|---|---|---|---|
| CMOCC-0026-VALERIO2016-source-sequence-2-comparison | READING_COMPARISON | The comparison names both source positions, but the Olivier side is reported through Valério rather than directly consulted. The two assertions are not independent confirmations. | Inspect the exact Olivier edition locus directly and assess the same physical position; published reassessment remains unadjudicated. |
| CMOCC-0026-VALERIO2016-source-sequence-5-comparison | READING_COMPARISON | The comparison names both source positions, but the Olivier side is reported through Valério rather than directly consulted. The two assertions are not independent confirmations. | Inspect the exact Olivier edition locus directly and assess the same physical position; published reassessment remains unadjudicated. |
| CMOCC-0027-VALERIO2016-source-first-sequence-3-comparison | READING_COMPARISON | The comparison names both source positions, but the Olivier side is reported through Valério rather than directly consulted. The two assertions are not independent confirmations. | Inspect the exact Olivier edition locus directly and assess the same physical position; published reassessment remains unadjudicated. |
| CM209-top-comparison | READING_COMPARISON | The comparison names both source positions, but the Olivier side is reported through Valério rather than directly consulted. The two assertions are not independent confirmations. | Inspect the exact Olivier edition locus directly and assess the same physical position; published reassessment remains unadjudicated. |
| CM209-ai201-comparison | READING_COMPARISON | The comparison names both source positions, but the Olivier side is reported through Valério rather than directly consulted. The two assertions are not independent confirmations. | Inspect the exact Olivier edition locus directly and assess the same physical position; published reassessment remains unadjudicated. |
| CM209-aii501-internal-comparison | READING_COMPARISON | Two incompatible labels occur within Valério’s own apparatus; neither is admitted at this position. | Reconcile table/commentary and critical re-edition at the exact cited pages before encoding this position. |

`research/attribution-review.json` pins every referenced native artifact by SHA-256 and records exact JSON pointers. `analysis/attribution-review-audit.json` is replayed by the checker. Queries reject changed input bytes before returning any case. The earlier native records remain unchanged.

Pair-attribution states describe documentary limitations, not scientific acceptance. A partial located comparison can be a real scholarly alternative without full typographic, physical-position or independent collation. `NOT_APPLICABLE` marks controls and interpretations for which a two-reading pair is not the appropriate unit. No unknown pair/witness total is replaced with zero.
