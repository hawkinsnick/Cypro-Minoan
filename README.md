# Cypro-Minoan Open Corpus

**Version 0.1.0 — corpus specification and scholarly infrastructure**

An open, provenance-first framework for building a machine-readable corpus of Cypro-Minoan inscriptions. Version 0.1.0 intentionally contains **infrastructure, not a copied corpus**: schemas, citation/provenance rules, research-ethics requirements, validation tooling, and templates for future inscription and sign records.

## Core principle

> The corpus records evidence; it does not encode a decipherment.

This project exists to support scholarship, not appropriate it. Published readings, sign identifications, classifications, drawings, photographs, and interpretations remain attributable to their authors and rights-holders. Every scholarly claim introduced into the corpus must retain enough provenance for a reader to identify its source.

## 0.1.0 scope

- Stable project data model for inscriptions, signs, attestations, classifications, and bibliography.
- Source-level provenance and uncertainty model.
- Explicit distinction among `published`, `independent_observation`, and `project_derived` assertions.
- JSON Schemas and validation script.
- Templates for future records; no claim that the corpus is populated or complete.
- Unicode support as a representation layer, not as the definition of the sign inventory.
- Framework for future Olivier/Ferrara/other concordances without asserting that competing systems are equivalent.

## Scholarly position

Cypro-Minoan is undeciphered. Sign identification, palaeographic grouping, traditional CM0/CM1/CM2/CM3 classification, readings, relationships with Linear A, and relationships among Cypro-Minoan varieties can be disputed. The database therefore stores claims together with their sources instead of silently resolving disagreements.

## Repository map

- `corpus/` — inscription records (empty in 0.1.0 except template)
- `signs/` — sign-record template and representation policy
- `schemas/` — machine-readable JSON Schemas
- `bibliography/` — source registry and starter bibliography
- `concordances/` — future cross-system mappings
- `docs/` — methodology, notation, roadmap, data dictionary
- `scripts/` — validators and utilities
- `tests/` — schema fixtures/tests

## Research ethics

Read [`RESEARCH_ETHICS.md`](RESEARCH_ETHICS.md) before contributing data. In short: credit scholarship, preserve disagreement, do not launder copied transcriptions into “data,” do not redistribute copyrighted images without permission, distinguish observation from interpretation, and make corrections transparently.

## Citation

See `CITATION.cff`. Individual records will also cite the scholarship from which their assertions derive. Citing this repository is not a substitute for citing the original scholars whose work a downstream analysis uses.

## License

Project-original code and original database structure are released under MIT (`LICENSE`). This license **does not and cannot relicense third-party scholarship, images, drawings, or text**. Future data records must carry source/rights metadata appropriate to their contents.

## Status

0.1.0 is a foundation release. It should not be cited as a complete corpus of Cypro-Minoan inscriptions.
