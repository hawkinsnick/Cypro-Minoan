# Selected source collation — 2026-10-15

Six selected comparisons rechecked against Valério’s rendered pages. Five original Olivier readings remain indirect because the needed2007 book pages were not acquired. The09/10 discrepancy remains real within Valério; its nearby commentary addresses the fourth sign59, not the second sign. Neither disputed label is admitted.

Scope: selected source-located tasks. This is a fresh, bounded publication check with a separate consultation state for every source. It is not a complete critical edition, exhaustive literature search, independent expert review or project examination of an ancient object.

## Findings and remaining work

| Task | Source observations | Remaining work |
|---|---|---|
| CMOCC-0026-VALERIO2016-source-sequence-2-comparison | Valério p.457 ##026 explicitly proposes75→73 at source-sequence position2. The original-side label is still reported through this secondary reassessment. | Consult Olivier p.76 directly; compare the exact source position and its uncertainty before any promotion. |
| CMOCC-0026-VALERIO2016-source-sequence-5-comparison | Valério p.457 ##026 explicitly proposes75→73 at source-sequence position5. The original-side label is still reported through this secondary reassessment. | Consult Olivier p.76 directly; compare the exact source position and its uncertainty before any promotion. |
| CMOCC-0027-VALERIO2016-source-first-sequence-3-comparison | Valério p.457 prints08→13 at ##027 third position; p.458 attributes the earlier08 to Olivier. No direct Olivier page was inspected. | Consult Olivier p.77; retain the original attribution as indirect until then. |
| CM209-top-comparison | The p.527 top-group correction13→08 agrees with the critical re-edition p.531 at the declared third position. | Olivier p.496 and exact physical-position collation remain unacquired/unadjudicated. |
| CM209-ai201-comparison | The p.528 A.I.2.01 correction27→10 is qualified by underlining and an adjacent lacuna; p.531 repeats the proposed10. | Retain source doubt and lacuna. Direct Olivier and damaged-sign assessment remain open. |
| CM209-aii501-internal-comparison | At A.II.5.01 second position, pp.532–533 print09; the p.534 critical re-edition prints10. The p.533 paragraph discusses confirmation of the fourth-position59 and does not explain this second-position change. | Neither second-position label is admitted. An authorial correction or qualified sign-level assessment is required; the last-sign discussion cannot settle09/10. |

## Consultation receipts

| Source | Modality | Inspected locus | Limits |
|---|---|---|---|
| [Jean-Pierre Olivier, with Frieda Vandenabeele (2007), Édition holistique des textes chypro-minoens, Biblioteca di Pasiphae6, Fabrizio Serra.](https://www.libraweb.net/index.php?chiave=2291&dettagliononpdf=1&h=436&name=Olivier.jpg&valore=sku&w=300) | BIBLIOGRAPHIC_ROUTE_ONLY | p.76, ##026; p.77, ##027; p.496, ##209 | Publisher web catalogue inspected via web retrieval: print editions/ISBNs and contents; no needed book pages acquired. Ordinary local HTTP returned403. No direct reading confirmation. |
| [Miguel Filipe Grandão Valério (2016), Investigating the Signs and Sounds of Cypro-Minoan, Universitat de Barcelona doctoral thesis.](https://diposit.ub.edu/server/api/core/bitstreams/1419cfea-e25f-44dd-9a8c-74e9836ae05e/content) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.457, ##026–027 (PDF ordinal463); p.458, continuation of ##027 (PDF ordinal464); p.527, ##209.A.I (PDF ordinal533); p.528, A.I.2.01 commentary (PDF ordinal534); p.531, critical re-edition A.I (PDF ordinal537); p.532, ##209.A.II (PDF ordinal538); p.533, A.II.5.01 commentary (PDF ordinal539); p.534, critical re-edition A.II (PDF ordinal540) | Direct inspection of Valério, not direct Olivier2007 consultation. Published images were inspected as page context; no independent sign adjudication. |

The JSON packet retains bibliographic identities, exact native comparison/check pointers, PDF byte hashes where acquired, and page-render hashes for inspected pages. PDF files, rendered page images and full protected editions are not redistributed. A web-text consultation has no PDF byte hash and cannot certify diacritics or figure details. Access failures are route-specific observations, not proof that lawful copies do not exist.

## Reproduce the integrity checks

```sh
python scripts/source_collation.py --check
python scripts/source_collation.py --case 'CMOCC-0026-VALERIO2016-source-sequence-2-comparison'
python -m unittest discover -s scripts -p test_source_collation.py
```

Researchers with a lawfully obtained copy can match it to an inspected PDF receipt using `python scripts/source_collation.py --verify-source SOURCE_ID /path/to/source.pdf`. A byte match establishes source version, not scholarly correctness or permission to redistribute it.

Canonical/frozen readings are unchanged. A correction to project source-attribution notation does not accept a reading. See `research/source-collation-2026-10-15.json` for case-specific source voices, uncertainty carriers and remaining work.
