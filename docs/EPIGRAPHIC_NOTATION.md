# Structured Epigraphic Notation — v0.2.0

The canonical representation is structured JSON, not punctuation embedded in a plain-text string.

Each sign token may record: `position`, `sign_ref`, `source_label`, `certainty`, `preservation`, `editorial_status`, `variant_note`, and `source_id`.

Controlled values:
- certainty: certain | probable | possible | uncertain | unidentified
- preservation: complete | damaged | fragmentary | lost | unclear
- editorial_status: observed | published_reading | restored | supplied | normalized
- boundary_after: none | separator_dot | separator_line | line_break | word_boundary_proposed | unknown

A lacuna is a segment with `segment_type: "lacuna"`; its extent is recorded as known count, range, or unknown. A restoration is never stored as if observed: it must carry `editorial_status: "restored"` and provenance.

Directionality is an inscription/line assertion with provenance. Unicode's left-to-right encoding behavior does not establish the physical direction of every inscription.

Plain-text exports are derived views and must never be the sole preservation of uncertainty.
