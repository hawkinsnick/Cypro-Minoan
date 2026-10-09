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
