---
name: cypro-minoan-research
description: Evidence-first AI research skill for the Cypro-Minoan corpus.
version: 0.3.1
---

# Cypro-Minoan Research Skill

This skill is an interface to the corpus in this repository. The corpus remains the canonical source of truth. Never maintain an independent scholarly dataset inside the skill.

## Governing rules
1. Separate physical/epigraphic observation, source transcription, normalization, computational derivation, scholarly interpretation, and AI-derived analysis.
2. Prefer canonical machine-readable corpus records over prose summaries for record-level questions.
3. Preserve identifiers, provenance, uncertainty, disagreements, corrections, negative results, and superseded analyses.
4. Never invent missing signs, readings, restorations, provenience, bibliography, source independence, or rights.
5. Label calculations performed by the AI and state enough method for reproduction.
6. Respect record/source-specific licensing and attribution. Repository-level licensing must not erase upstream restrictions.
7. For cross-corpus claims, establish comparability and source independence before interpreting similarity.
8. Report blocked or missing evidence rather than filling gaps.

## Corpus-specific caution
Undeciphered script: do not convert sign correspondences, recurring sequences, positional patterns, or proposed values into established readings or language identification.

## Default research response
Give the direct answer, followed as relevant by Evidence; Evidentiary status; Uncertainty/limitations; Reproducibility; Rights/attribution.

## Synchronization
Read `ai-skill/generated/source-state.json` before substantive work. It records the corpus commit from which the AI-facing package was synchronized. Generated files are rebuildable views; canonical corpus files govern if a discrepancy is found.

## Academic-scrutiny gates
- Corpus-wide sign frequency remains BLOCKED until canonical status changes
- Cross-script phonetic inference remains BLOCKED
- Primary and dependent-secondary occurrences must not be counted as independent witnesses
- Interchange mappings do not redefine native Cypro-Minoan evidence

## Context and dossier routing
Read `analysis/context-coverage-v1.json` and `research/record-dossiers.json` before record-level context or coverage claims. Follow native references, source IDs, locators and input digests. Separate metadata coverage from reading/occurrence coverage. Preserve literal unknowns, alternative script classifications and chronology qualifiers. Treat missing evidence as unknown. Do not upgrade source-reported catalogue links to physical identity, partial occurrences to complete transcriptions, or source closure to independent verification. Consult `docs/CONTEXT-AND-DOSSIERS.md` for the specific acquisition and rights limits.


## Offline corpus browser
Run `python scripts/build_corpus_browser.py` to generate `workbench/corpus-browser.html`. The browser is self-contained and searches only the explicitly allowlisted files in `research/browser-sources.json`. Adding a file to the browser requires a rights/provenance check; never recursively ingest repository data or restricted upstream material. Browser display does not establish decipherment, source independence, or expert validation.


## Fleet EpiDoc and identity graph gates
Read `analysis/epidoc-interoperability-audit.json` and `research/identity-graph.json`. EpiDoc serialization must preserve object/surface/text distinctions, partial occurrence coverage, authority-specific sign labels and source dependence. Never serialize a potmark as linguistic text merely because it bears a mark, and never turn a sign-label correspondence into a phonetic or physical identity assertion.

## EpiDoc pilot execution
For EpiDoc interchange, use `scripts/export_epidoc_occurrences.py` and read `docs/EPIDOC-PILOT.md`. The generated XML is a partial, source-assertion view only. Preserve source-qualified published sign labels, source roles, certainty, locators and zone boundaries. The occurrence pilot passed EpiDoc 9.8 Relax NG and exporter-canonical artifact checks (GitHub Actions run 37718674499); this does not establish full EpiDoc conformance, Schematron validation, full object coverage, or epigraphic correctness. Canonical `certain` is serialized as `cert="high"` with `#canonical-certainty-certain` retained in `@ana`; always consult canonical JSON for the source category.

## Upstream EpiDoc pilot validation

Read `analysis/upstream-epidoc-validation.json`, `interchange/epidoc/upstream-pins.json` and `docs/EPIDOC-PILOT.md`. All 57 embedded upstream Schematron patterns and pinned Relax NG now execute against the 16-occurrence partial pilot. Full corpus coverage, independent review and external authority resolution remain open. Replay the documented validator before a conformance claim; every upstream finding blocks this strict pilot profile.

For current catalogue reconciliation, consult `catalogues/source-located-concordance.json`, `analysis/catalogue-mapping-audit.json` and `docs/CATALOGUE-CONCORDANCE.md`. All 254 controlled slots now have source-attributed sigla, including 186 newly resolved mappings. Preserve `source_label`, the asterisk marker and `ENKO?`; the marker meaning is NOT_ADJUDICATED. A source-reported namespace join is neither physical-object certification nor an independent witness or sign reading. The current source checkpoint has 21 rich records, 16 occurrences on nine records and 12 currently uncovered records. The original 15-record review cohort remains a dated baseline with three records now partially source encoded. Historical release audits retain their historical 68/254 counts.

The fifteen uncovered rich records now have record-specific source dispositions and blank review decisions in `research/uncovered-record-review-controls.json`. Eight have visually inspected dependent-edition locators; four Met candidates have 14 inspected, hash-pinned CC0 photographic views (`research/met-open-image-controls.json`). Two retain metadata-only acquisition routes and one official source currently returns HTTP403. Consult `docs/UNCOVERED-RECORD-REVIEW.md`; retain possible/alternative script classifications, source dependence and UNREVIEWED decisions. No sign readings or expert review have been added.

## Bounded source checkpoint (2026-10-11)

Use `research/source-check-2026-10-11.json`, `research/source-reconciliation.json` and `research/coverage-denominators.json` together. Retain source roles, unresolved competing labels/materials and literal identifier namespaces. Never sum overlapping catalogue and rich-record views, infer a physical corpus population, or promote dependent evidence to independent primary verification.

## Existing evidence: reconciliation and identity controls

Before source certainty, apparatus, duplicate or object-identity claims, read `research/reference-reconciliation-v2.json`, `research/identity-reconciliation-v2.json` and `docs/EXISTING-EVIDENCE-RECONCILIATION.md`. Literal source strings are frozen; read the apparatus ledger alongside them. Primary agreement of numeric labels is not independent sign verification. Unidentified marks and conditional alternatives are not added canonical occurrences. Namespaces and core/candidate status cannot be flattened, and zero exact alias collisions cannot establish physical uniqueness.

Selected Donnelly 2020 pp. 104–105 and Fig. 3 now confirm the attribution already encoded for Louvre AM 1639. Consult `research/donnelly-existing-assertion-check.json`; retain probable source status and the figure’s Masson lineage. Comparisons with ADD##219 do not establish object identity; no numbered join or new occurrence was added.
