# Architecture 3.0

## Stable layers
**Evidence:** objects/documents, physical loci/zones, source-verified occurrences, context assertions and attributed representations.

**Witnesses:** source assertions, source lineage/independence, disagreements, corrections and supersessions.

**Research:** catalogue snapshots/reconciliation, signary authorities, corpus policies, dataset snapshots, experiment specifications/gates, typed comparative hypotheses, claims/results/errata.

**Interchange:** canonical record-level Aegean Epigraphy Interchange v0.1 plus CM collection adapters; Research API v1 read contract.

**Clients:** CLI/Python/UI/export consumers. Clients never redefine corpus truth.

## Dependency direction
Clients → interchange → research/evidence → provenance/source records. Interpretive hypotheses may depend on observations; observations may not depend on interpretations.

## 3.0 stability promise
Breaking changes to stable interchange contracts require a versioned successor. Native CM schemas may evolve with evidence and migrations. A field is not promoted to shared core merely because one script needs it.

## Non-goals
3.0 does not claim corpus completeness, decipherment, phonetic proof, complete transcription coverage, complete palaeographic-variant population, or corpus-wide statistical inference while occurrence coverage remains sparse.
