# Architecture 2.0

## Stable layers
**Evidence:** objects/documents, physical loci/zones, occurrences, source-defined structural units, context assertions.

**Witnesses:** object identity, source assertions, source lineage, disagreements/adjudication.

**Research:** catalogue snapshots, signary authorities, corpus policies, typed concordance hypotheses, experiment gates, claims/results/errata.

**Interchange:** Research API v1-compatible read contract and Aegean Epigraphy Interchange v0.1.

**Clients:** future CLI/Python/UI/export adapters. Clients do not redefine corpus truth.

## Dependency direction
Clients → interchange → research/evidence layers → provenance/source records. Interpretive hypotheses may depend on observations. Observations may not depend on interpretive hypotheses.

## Stability promise
Breaking changes to stable interchange contracts require a versioned successor. CM-native schemas may evolve when evidence requires it, with migration/provenance.

## Explicit non-goals
2.0 does not claim corpus completeness, decipherment, phonetic proof, language identification, independence where source lineage is shared, or statistical conclusions from insufficient occurrence coverage.
