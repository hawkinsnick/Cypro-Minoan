# Contributing

Contributions are welcome from specialists, students, developers, museums, and interested researchers. Read `RESEARCH_ETHICS.md` first.

## Data contributions

1. Create or edit a record using the schemas in `schemas/`.
2. Add every cited source to `bibliography/sources.json`.
3. Attach provenance to source-derived assertions.
4. Mark damaged, uncertain, restored, or disputed material explicitly; never “clean up” uncertainty.
5. Do not add images or substantial source text unless reuse rights are documented.
6. Run `python scripts/validate.py` before submitting.

## Scholarly disagreement

A pull request does not need to establish that one scholar is correct. If two documented readings conflict, model both. Discussion should address evidence, data representation, and sources rather than personalities.

## Corrections

Corrections should state what changed, the evidence supporting the change, and whether the change affects project normalization or a source-specific assertion. Never rewrite a published scholar's reading to make it agree with ours; add a separate assertion.
