## Unreleased — EpiDoc occurrence interoperability pilot (2026-10-07)

- Added a loss-aware exporter for the 12 source-checked occurrence assertions; partial coverage must not be read as a complete transcription.
- Preserved source-qualified published sign labels, source roles, certainty, locators, zone boundaries, and explicit potmark caution.
- Added invariant tests and researcher documentation for the occurrence-layer pilot.
- Pinned the external validation target to EpiDoc 9.8 (`v9.8`, release commit `5655fb778ecc93a4b6a7346995a55ea686a9e9b2`, TEI 4.10.2 alignment).
- EpiDoc validation has **not yet been executed**; no conformance claim is made. Full object-level EpiDoc description remains outside the current occurrence-layer scope.

## 5.2.5 — mapping/statistical repair and stronger scientific-claim guards

21 rich records and 9 source-checked occurrences. Three clay-ball occurrences carry primary-publication locators. Corpus-wide frequency and cross-script phonetic claims remain blocked.

## 5.2.4 — current-state integrity and evidence gate reconciliation

- Repair malformed schemas and enforce schema semantics with positive/negative fixtures.
- Replace obsolete release-number assertions with evidence and current-metadata checks.
- Synchronize current citation, family and native index/API/manifest metadata while preserving historical content versions.
- 21 rich records and 9 source-checked occurrences. Three clay-ball occurrences carry primary-publication locators. Corpus-wide frequency and cross-script phonetic claims remain blocked.

# Changelog

## [5.0.0] - 2026-09-28
- Added question-specific research-readiness profiles; no global analysis-ready flag.
- Added materialized evidence graph and graph contract with gate-aware claim support.
- Added immutable release-scoped dataset snapshot succession.
- Added dependency-direction contract across clients/interchange/research/evidence/provenance.
- Added assertion provenance ledger and explicit witness-independence counting policy.
- Added representation-level rights policy.
- Added positive and negative epistemic conformance fixtures and CI tests.
- Added 5.0 validator, architecture, audit and release criteria.
- Preserved BLOCKED status for corpus-wide frequency and cross-script phonetic inference.
- Added no synthetic sigla, transcriptions, variants or frontier objects to satisfy the major release.

## [4.0.1] - 2026-09-28
- Repaired reproducibility-profile/result-schema contradiction by defining and requiring `software_or_script` and `experiment_gate`.
- CI now runs the current major-release validator and release-integrity regression tests in addition to foundation validation.
- Added regression checks for blocked experiment claims and stale API fixture versions.
- Updated Research API examples, citation metadata and coverage documentation to the current release.
- Clarified current-release wording in the claim registry without changing scholarly evidence.
- No new inscriptions, readings, sign variants or inferential claims were added.

## [4.0.0] - 2026-09-27
- Added machine-readable multidimensional completeness matrix; aggregate completeness scores prohibited.
- Added prioritized evidence-acquisition queue and prohibited-shortcut registry.
- Added open-world frontier policy.
- Added reproducibility profile and evidence-package definitions with per-input hashing utility.
- Added sensitivity matrix and comparative null/control registry.
- Added typed comparative-hypothesis registry with non-transitivity as default.
- Added reproducible research-result schema and executable claim-gate checker.
- Added shared-core candidate boundary derived only from semantics proven in Linear A and Cypro-Minoan.
- Added Architecture 4.0, release criteria, adversarial validator and explicit incomplete-evidence audit.
- Preserved blocked corpus-frequency and phonetic experiments rather than manufacturing evidence.

### 3.9 → 4.0 maturation
Adversarial audit → reproducibility enforcement → completeness accounting → comparative controls → shared-core boundary → stable 4.0 platform.

## [3.0.0] - 2026-09-27
- Evidence research platform with catalogue reconciliation, frontier registry, witnesses, occurrence/palaeographic architecture, dataset snapshots and experiment gates.


## 5.3.0 — context and review dossiers

Adds eight date/period assertions on four Met records, closes nine missing bibliography references with explicit access/verification limits, and generates dossiers for all 21 rich records plus accounting for 254 catalogue slots. Twelve occurrences on six records remain unchanged; partial positions are not full transcriptions.

Adds source-reference closure checks, full dossier/coverage replay and hostile tests for orphan sources, duplicate identities and metadata-to-reading promotion. Existing scientific gates retain their prior state.

## Unreleased — 2026-10-11 source checkpoint

Four partial Valério 2016 assertions were checked on printed pp. 457–458 (PDF 463–464) and encoded on CMOC-0025, 0026 and 0027. The total is 16 occurrences on nine of 21 rich records: six primary-publication and ten dependent-secondary assertions. Twelve rich records still lack encoded occurrences. Three positional reassessments retain reported Olivier labels 75/75/08 beside Valério proposals 73/73/13, without treating the uninspected Olivier edition as verified. The EpiDoc exporter now preserves editorial notes, preventing loss of alternatives. The original 15-record expert packet remains a dated cohort, with the three newly partial records accounted separately. Exactly 14 rich records have explicit catalogue joins, 240 of 254 slots lack a rich join, and seven rich records have unresolved catalogue joins. None of these numbers is a physical-inscription population.

## Existing-evidence reconciliation — 2026-10-11

Reading coverage is unchanged. [Existing-evidence reconciliation](docs/EXISTING-EVIDENCE-RECONCILIATION.md) now accounts for every existing assertion and identity, preserving source apparatus and unresolved scholarly decisions.

Selected Donnelly 2020 pp. 104–105 and Fig. 3 now confirm the attribution already encoded for Louvre AM 1639. Consult `research/donnelly-existing-assertion-check.json`; retain probable source status and the figure’s Masson lineage. Comparisons with ADD##219 do not establish object identity; no numbered join or new occurrence was added.

## Unreleased — AI integrity checkpoint

Require checked native dependency projections, preserve corpus-native bundle schemas, and publish synchronized bundles only on their validated source parent. Add Git race and hostile dependency tests; no new readings or expert acceptance.


### Source coverage and reconciliation — 2026-10-12

Replayed nine exact Louvre inventory/edition joins and inspected primary context for the Tiryns clay ball, preserving damaged-sign and database-identifier qualifications. No new reading or independent review. See [scope, rights and verification](docs/SOURCE-GROWTH-2026-10-12.md).

## 2026-10-14 — ten finite dependent source assertions
Added source-located numerical positions on CMOC-0028, CMOC-0032 and CMOC-0033. Prior sixteen assertions preserved; coverage is 26 assertions on 12/21 records, with nine unencoded. No primary certification, source independence or expert acceptance. Regenerated dossiers, qualified views, coverage and interchange controls.

## CMOC-0209 source checkpoint — 14 October 2026

See [CMOC-0209 source check](docs/CMOC-0209-SOURCE-CHECK.md). Current coverage is 28 source assertions on 13/21 rich records, with eight lacking encoded positions. Only two CMOC-0209 positions are added; one remains uncertain. Preserve reported originals and the unresolved internal 09/10 disagreement; do not select either internally conflicting label, infer full-tablet coverage, or claim primary collation/expert acceptance. Earlier dated checkpoints remain historical.

## 2026-10-15 — Native evidence and alternative-reading queries

Added pinned native evidence profiles, exact-ID/JSON-pointer queries, coverage replay, loss/corruption/identity/path tests and CI. Updated researcher documentation, AI instructions and evidence bundle indexing. Existing source data and scientific acceptance states are unchanged.

## 2026-10-15 — Selected source collation

Six selected comparisons rechecked against Valério’s rendered pages. Five original Olivier readings remain indirect because the needed2007 book pages were not acquired. The09/10 discrepancy remains real within Valério; its nearby commentary addresses the fourth sign59, not the second sign. Neither disputed label is admitted. Frozen readings and independent-review status remain unchanged.

## 2026-10-17 — Research delivery controls

Add checksum-bound native search/evidence responses, deterministic local research
packaging and offline replay, revision-bound review submission forms and rejection
tests. Update individual AI instructions and documentation. No source record,
reading, expert acceptance or redistribution permission is added by this change.


### 2026-10-18 source acquisition follow-up

Pursued the requested sources and recorded bounded consultation/access results, source-identity checks and unsent delivery requests. New source-intake tasks are queryable and included in collection/AI routing. Original-page typography work remains open; frozen readings unchanged.
