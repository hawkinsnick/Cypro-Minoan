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

## Validation boundary

The invariant test checks the project's loss-prevention rules. Formal validation
against an externally pinned EpiDoc schema/profile remains a separate gate and must
be added before the repository claims EpiDoc conformance.
