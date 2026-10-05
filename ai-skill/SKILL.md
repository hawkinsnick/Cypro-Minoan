---
name: cypro-minoan-research
description: Evidence-first AI research skill for the Cypro-Minoan corpus.
version: 0.3.1
---

# Cypro-Minoan Research Skill

This skill is an interface to the corpus in this repository. The corpus remains the canonical source of truth. Never maintain an independent scholarly dataset inside the skill.

## Governing rules
1. Separate physical/epigraphic observation, source transcription, normalization, computational derivation, scholarly interpretation, and AI-derived analysis.
2. Prefer canonical machine-readable corpus records over prose summaries for record-level questions.
3. Preserve identifiers, provenance, uncertainty, disagreements, corrections, negative results, and superseded analyses.
4. Never invent missing signs, readings, restorations, provenience, bibliography, source independence, or rights.
5. Label calculations performed by the AI and state enough method for reproduction.
6. Respect record/source-specific licensing and attribution. Repository-level licensing must not erase upstream restrictions.
7. For cross-corpus claims, establish comparability and source independence before interpreting similarity.
8. Report blocked or missing evidence rather than filling gaps.

## Corpus-specific caution
Undeciphered script: do not convert sign correspondences, recurring sequences, positional patterns, or proposed values into established readings or language identification.

## Default research response
Give the direct answer, followed as relevant by Evidence; Evidentiary status; Uncertainty/limitations; Reproducibility; Rights/attribution.

## Synchronization
Read `ai-skill/generated/source-state.json` before substantive work. It records the corpus commit from which the AI-facing package was synchronized. Generated files are rebuildable views; canonical corpus files govern if a discrepancy is found.

## Academic-scrutiny gates
- Corpus-wide sign frequency remains BLOCKED until canonical status changes
- Cross-script phonetic inference remains BLOCKED
- Primary and dependent-secondary occurrences must not be counted as independent witnesses
- Interchange mappings do not redefine native Cypro-Minoan evidence

## Context and dossier routing
Read `analysis/context-coverage-v1.json` and `research/record-dossiers.json` before record-level context or coverage claims. Follow native references, source IDs, locators and input digests. Separate metadata coverage from reading/occurrence coverage. Preserve literal unknowns, alternative script classifications and chronology qualifiers. Treat missing evidence as unknown. Do not upgrade source-reported catalogue links to physical identity, partial occurrences to complete transcriptions, or source closure to independent verification. Consult `docs/CONTEXT-AND-DOSSIERS.md` for the specific acquisition and rights limits.
