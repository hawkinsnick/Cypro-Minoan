# Aegean Epigraphy Interoperability Contract — v0.1

Cypro-Minoan and Linear A remain independent scholarly corpora. This contract defines only their decipherment-neutral intersection for future shared tooling.

Shared concepts are: stable project-local records; source-attributed identifiers; assertions rather than unqualified values; provenance and transformations; explicit uncertainty; rights; source/evidence lineage; physical loci; attributed representations; and hypotheses kept outside observational ground truth.

## Required invariants
- Credit follows claims.
- Digital re-encoding does not create independent epigraphic evidence.
- Competing responsible assertions may coexist.
- Project-derived normalization identifies its inputs.
- Rights travel with derived records/material.
- Script identity, sign identity, phonetic value and linguistic interpretation remain separate.
- Missing evidence is not filled merely for schema compatibility.
- Corrections/supersessions are versioned.
- Comparative tools use adapters rather than assuming either corpus's native model.

## Cypro-Minoan mapping
- record → CMOC inscription record
- assertion → `schemas/assertion.schema.json`
- provenance → assertion `provenance`
- representation → attributed `transcriptions[].segments`
- rights → record `rights`
- hypothesis → concordance/analysis layers

## Non-equivalences
CM0/CM1/CM2/CM3 remain attributed Cypro-Minoan classifications, not cross-script categories. `CMSIGN` concepts are not Linear A AB signs. Cypro-Minoan segmentation does not inherit Linear A's SigLA source-defined Word object. Future Linear B phonetic/morphological categories are optional extensions, not shared-core requirements.

The full cross-project roadmap is mirrored in `hawkinsnick/Linear-A`.
