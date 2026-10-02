#!/usr/bin/env python3
"""Scholarly-boundary regression tests for the current Cypro-Minoan evidence layer."""
import json
import pathlib

R = pathlib.Path(__file__).resolve().parents[1]
load = lambda p: json.loads((R / p).read_text(encoding="utf-8"))

state = load("analysis/current-status.json")
coverage = load("analysis/occurrence-coverage-v1.json")
queue = load("research/expert-review-queue.json")
gates = load("research/experiment-gates.json")["experiments"]

assert state["committed_evidence_counts"]["rich_records"] == coverage["rich_records"] == 21
assert state["committed_evidence_counts"]["source_checked_occurrences"] == coverage["encoded_occurrences"] == 9
assert coverage["records_with_encoded_occurrences"] + len(coverage["records_without_encoded_occurrences"]) == coverage["rich_records"]
assert coverage["sign_labels_merged"] is False
assert coverage["witness_independence_established"] is False
assert coverage["corpus_wide_frequency_allowed"] is False
assert state["scientific_results"]["corpus_wide_frequency"] == "BLOCKED"
assert state["scientific_results"]["cross_script_phonetic_test"] == "BLOCKED"
assert all(g["claim_allowed"] is False for g in gates if g["state"] == "BLOCKED")
assert queue["items"]
assert "frequency" in queue["admission_rule"].lower()
assert "phonetic" in queue["admission_rule"].lower()
print(json.dumps({"status":"PASS","rich_records":21,"encoded_occurrences":9,"blocked_claims_preserved":True}))
