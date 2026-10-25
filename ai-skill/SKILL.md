---
name: cypro-minoan-research
description: Evidence-first AI research skill for the Cypro-Minoan corpus.
version: 0.3.1
---

## Load and validate this repository-bound skill

Use this file as the canonical individual skill. Load the complete matching
repository checkout or give the AI access to its files; this Markdown file alone
contains instructions, not the corpus. Do not claim that supplying a GitHub URL
installs a skill or makes private/local files available to an AI platform.
Resolve the paths below from the repository root. With Python 3.10+ available,
run `python scripts/validate_ai_skill.py` before describing this skill as
operational on the supplied checkout. Read `docs/AI-SKILL-VALIDATION.md` for the
exact workflow, examples, dependencies, validation scope and limitations.
If execution or source access is unavailable, say which step was not run and
make no fresh validation claim. Preserve all native source/rights restrictions.

Discover exact IDs with `python scripts/evidence_query.py --coverage` and
`python scripts/evidence_query.py --list COLLECTION`. Retrieve evidence with
`python scripts/evidence_query.py --record ID --collection COLLECTION`;
use `python scripts/research_delivery.py --dossier ID --collection COLLECTION`
for its evidence-only answer frame. Return the exact source path/hash/pointer,
attribution, uncertainty and native evidence unit. A missing ID means absent
from the selected view; never invent a replacement or infer global absence.


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

## Enforced assertion, dependency and bundle integrity

Read `docs/AI-INTEGRITY.md` and the required `research/cross-corpus-dependencies.json` before source counts or cross-corpus analysis. Use qualified assertion views when provided; original source literals must travel with their reconciliation, uncertainty and identity context. The dependency register does not certify physical identity or linguistic affinity. Shared catalogue references and duplicated digital sources are not independent witnesses. Missing links mean unknown, not independent. `scripts/check_cross_corpus_dependencies.py` screens declared record selections and rejects pooled physical/witness counts and phonetic transfer. Native AI bundle validation checks the dependency projection and local evidence hashes. Bundle publication validates the exact source parent and never rebases or force-pushes the validated artifact. Software and packaging checks do not establish expert or model-behavior acceptance.


## Source growth — 2026-10-12

Read `docs/SOURCE-GROWTH-2026-10-12.md` and `analysis/source-growth-2026-10-12.json` with `research/louvre-object-concordance.json`, `research/tiryns-clay-ball-primary-context.json`. Join museum facts by inventory plus source edition numbers; nearby ARKs and numeric order are not identity evidence. TN 241 is a Tracing Networks database ID, not TN 2413 or a museum accession. Preserve source ranges, damaged signs and distinct publication/digital dates. Source-count agreement is not an independent ancient witness. No glyph/reading admission or calibration is granted.

The Tiryns appendix’s `3 (?) signs` qualifier and VB/VC coordinate difference are explicit source assertions. Preserve both printed locators and unresolved status; do not replace the count with an unqualified three or adjudicate the coordinate.

## Current finite source growth — 2026-10-14
Read `docs/SOURCE-GROWTH-2026-10-14.md` and `research/source-growth-2026-10-14.json`. Prefer current 26 source assertions on 12/21 rich records (six primary, twenty dependent) over the historical 16-on-nine checkpoint. Keep nine unencoded records explicit. Ten additions on CMOC-0028/0032/0033 preserve numerical source order and the prior sixteen assertions unchanged. Source-encoding certainty is not independent graphical acceptance, full physical coverage or reading direction. Olivier locators are reported through Valério, not direct primary collation. Retain all historical disagreements and blank reviewer decisions; do not treat source growth as a redistribution licence, independent witnesses, corpus-wide frequency readiness or expert-only completion.

## CMOC-0209 source checkpoint — 14 October 2026

See [CMOC-0209 source check](../docs/CMOC-0209-SOURCE-CHECK.md). Current coverage is 28 source assertions on 13/21 rich records, with eight lacking encoded positions. Only two CMOC-0209 positions are added; one remains uncertain. Preserve reported originals and the unresolved internal 09/10 disagreement; do not select either internally conflicting label, infer full-tablet coverage, or claim primary collation/expert acceptance. Earlier dated checkpoints remain historical.

## Corpus-native evidence and alternatives

Read `docs/EVIDENCE-AND-ALTERNATIVES.md`, `research/evidence-query-profile.json` and `analysis/evidence-query-coverage.json` for evidence or competing-reading questions. Use `scripts/evidence_query.py` with exact native IDs and an explicit collection when ambiguous. Preserve `native_record`, every uncertainty/editorial mark, source attribution, locator, inspection status and rights. Cite artifact path, JSON pointer and SHA-256; hashes certify bytes only. Treat explicitly linked records as declared ID associations, not physical certification or independent witnesses. Context resources have corpus-level scope and are not automatically about the queried record. Distinguish a named source reading from a legacy queue label, uninspected bibliographic lead, count convention or hypothesis. Do not infer a count of collated alternative pairs or independent witnesses from searchable rows; those metrics remain unknown. Report the native units and scope of each view separately, and defer to the corpus-specific limits. No new readings, expert acceptance or decipherment follows from this interface.

## Bounded attribution review (2026-10-15)

Read `docs/ATTRIBUTION-REVIEW.md` and `research/attribution-review.json` before describing a dispute or source comparison. Run `python scripts/attribution_review.py --case ID` with the referenced evidence available. Preserve complete native evidence and distinguish reading, interpretation, classification, count, identity and representation questions. This checkpoint reviews pinned repository packets; it does not repeat their primary consultation or grant independent review. Inherit the exact author/publication, locator, consultation limits and dependence from each pointer; missing fields remain unknown. Use the case-specific remaining work. Do not count register entries or apparatus notes as fully attributed pairs, physical objects or independent witnesses.

All six comparisons: five reassessments have an indirect Olivier side; one is an internal Valério inconsistency. Direct consultation and independence are separate questions.

## Selected publication collation (2026-10-15)

Consult `research/source-collation-2026-10-15.json` and `docs/SOURCE-COLLATION-2026-10-15.md` for the selected source comparisons. Use `python scripts/source_collation.py --case ID` to retrieve the fresh source observations beside complete native evidence. Preserve printed forms, project notation and author-prose uncertainty as separate fields. Treat web text, rendered PDF inspection, indirect reports and bibliography-only access as distinct modalities. Do not infer direct edition access from a quoted source, physical autopsy from an author’s report, or acceptance from a successful integrity check.

Six selected comparisons rechecked against Valério’s rendered pages. Five original Olivier readings remain indirect because the needed2007 book pages were not acquired. The09/10 discrepancy remains real within Valério; its nearby commentary addresses the fourth sign59, not the second sign. Neither disputed label is admitted.

## Research delivery, evidence answers and feedback

Read `docs/RESEARCH-DELIVERY.md` and verify `analysis/research-delivery.json`
with `python scripts/research_delivery.py --check` before using delivery claims.
Use `--dossier ID --collection COLLECTION` for exact evidence-bound answers;
preserve the complete native payload, citations, categories and limitations.
Use `--search TEXT` for source-record retrieval. Do not convert file pointers
into missing primary-edition citations, catalogue rows into unique objects,
source dependence into independent confirmation, or review forms into acceptance.
Prepare bounded review drafts with `--review-template`; validate submissions with
`--validate-review`, then require native human-maintainer acceptance. Treat delivery
and deterministic answer tests as engineering checks, not empirical LLM validation
or completion of scholarly/source-permission work. Local packaging grants no new
redistribution rights. Label any model-generated analysis separately and cite it.


## Source intake status — 2026-10-18

Read `docs/SOURCE-INTAKE-2026-10-18.md` and `research/source-intake-2026-10-18.json` before reporting source completion. Preserve partial consultation versus unacquired original-page checks, corrected bibliographic identities, source-specific conventions and unchanged historical receipts. Request drafts are unsent; no purchase, accepted reading, extra witness or independent review follows.

## Verified physical-volume locator (2026-10-18)

The BnF catalogue reports Olivier2007 under FRBNF41246930, hardback ISBN9788862270304, shelfmark487.1 OLIV e (Tolbiac, Salle L). The native intake packet retains the exact catalogue and reproduction-service links. This is a delivery lead, not acquired edition pages, verified service eligibility or a sign reading. No request was submitted; the five indirect Olivier comparison sides remain indirect.

## Bounded printed-publication recheck

Read `docs/SOURCE-RECHECK-2026-10-21.md` and its receipt before reporting the
latest documentary check on CMOC-TIRY-ADD244. The three source catalogue labels
were compared with the rendered publication pages; no glyph, phonetic value,
independent witness or expert gate was certified. Run
`python scripts/validate_source_recheck_20261021.py` to replay the native match.

## Preserve review provenance

Reject malformed JSON-pointer escapes and negative or leading-zero array indices
when verifying source citations; literal object keys retain their own spelling.
Read the [master hostile-review report](https://github.com/hawkinsnick/Master-Corpus-AI-Skill/blob/main/references/hostile-review-2026-10-25.md)
for this member's pinned retrieval scope and the limits of the source-fidelity
and development checks. Complete retrieval-view traversal does not certify
corpus completeness, accepted readings, independent witnesses or expert review.
