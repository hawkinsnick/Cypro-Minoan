# Data Model

## Evidence first

The atomic scholarly unit is an **assertion with provenance**, not an unqualified database value. Convenient normalized fields may be added later, but they must be derivable from attributed assertions.

## Stable internal IDs

`CMOC-nnnn` identifies a project inscription record. `CMSIGN-nnn` identifies a project sign concept. Neither ID claims equivalence with any published catalogue/sign-list number.

## Transcriptions

Multiple transcriptions may coexist. Each carries `status`, `source_id`, locator, normalization note, and segments. A future normalized transcription must be `project_derived` and identify its inputs.

## Classification

CM0/CM1/CM2/CM3 and alternative classifications are stored as attributed assertions. They are not structural partitions of the database.

## Uncertainty

Use explicit uncertainty rather than silently selecting a reading. Damage, restoration, uncertain sign identity, uncertain direction, and disputed segmentation will receive structured representations in later releases.
