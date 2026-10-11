# EpiDoc occurrence pilot

The pilot exporter at `scripts/export_epidoc_occurrences.py` creates an EpiDoc/TEI
interchange view from the canonical source-checked occurrence assertions.

## Scope

This is deliberately **not** a complete transcription. Each exported `<g>` preserves
the published sign label, source authority, source role, certainty, position and
locator. Authority-specific labels are expressed with source-qualified URNs rather
than silently normalized.

Zones are serialized independently. A zone whose identifier contains `potmark` is
explicitly marked `#nonlinguistic-status-undetermined`; the exporter does not infer
that a mark is linguistic text. Dependent-secondary assertions remain marked as such.

## Reproducibility

Run:

```bash
python scripts/export_epidoc_occurrences.py
python tests/test_epidoc_occurrences.py
```

The generated XML is written to `interchange/epidoc/occurrences-pilot.xml`. Generated
XML is an interchange view, not a new scholarly authority. Canonical JSON and its
source/provenance metadata continue to govern.

## Certainty mapping

The canonical source assertion `certainty: "certain"` is represented by the
EpiDoc 9.8 Relax NG vocabulary `cert="high"`. These categories are not
semantically identical: the original category is retained as
`ana="#canonical-certainty-certain"` alongside the source-role annotation.
Canonical JSON is unchanged. Unrecognized certainty categories cause exporter
failure rather than silent coercion.

## Validation boundary

The invariant tests, EpiDoc 9.8 Relax NG validation using Jing, and exact
regeneration of the committed XML passed in GitHub Actions on
2026-10-07 (run 37718674499; commit `fb4db8f`).
This establishes **Relax NG validation of the occurrence pilot only**.
Schematron checks, upstream schema digest pinning, reference resolution,
full object-level coverage, and human epigraphic review are separate gates;
do not claim comprehensive EpiDoc conformance or complete transcription.

## Additional integrity gates (2026-10-08)

PR #11 added deterministic XML ID, local reference, source-locator, and partial-coverage checks; PR #12 added an executable **project-specific ISO Schematron** profile at `interchange/epidoc/pilot-integrity.sch`. Both were merged after green pull-request CI. Run `python tests/test_epidoc_reference_integrity.py` and, with `lxml` installed, `python tests/test_epidoc_schematron.py`.

These project gates validate the **partial occurrence pilot**. As of 2026-10-11, `scripts/validate_upstream_epidoc.py` also verifies expected upstream schema/compiler digests, Relax NG, and all 57 embedded EpiDoc 9.8 Schematron patterns using ISO compilation and Saxon XSLT 2. Every assertion failure or report blocks acceptance. `analysis/upstream-epidoc-validation.json` records 24 fired rules with no findings. Negative tests reject altered schemas/compilers and a contradictory date that triggers an upstream nonfatal report. External authority resolution, full object coverage and independent review remain open. No broader corpus conformance claim is made.

## Reproduce upstream validation

CI fetches EpiDoc/Source at `2368ee115d8008b32c37446301874945bcbe6c18` and Schematron/schematron at `77dcd36c53d12ed786c144ece3b2af7694abdc56`. Sources are used locally under their upstream terms and are not vendored. Install `lxml>=5,<7` and `saxonche==12.9.0`, then run `python scripts/validate_upstream_epidoc.py --schema /path/to/schema/9.8/tei-epidoc.rng --compiler /path/to/trunk/schematron/code`. Set `EPIDOC_SCHEMA` and `SCHEMATRON_COMPILER` to these paths to run `python -m unittest discover -s tests -p test_upstream_epidoc.py`.
