# Cross-Script Concordance Policy — v0.5.0

The concordance layer records **claims about relationships**, not deciphered values. It is deliberately separate from inscription evidence.

Relationship types: `graphic_similarity`, `historical_derivation`, `phonetic_equivalence_proposed`, `functional_equivalence`, `encoding_unification`, and `numeric_identity`.

Concordances are **not transitive**. If A resembles B and B has value /x/, the database must not infer that A has /x/. Historical derivation does not automatically imply graphic or phonetic identity. Every claim requires a source and exact locator; proposed phonetic equivalence also requires a named proponent.
