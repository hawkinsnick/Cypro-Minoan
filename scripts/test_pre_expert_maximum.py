#!/usr/bin/env python3
import json, pathlib
R=pathlib.Path(__file__).resolve().parents[1]
load=lambda p:json.loads((R/p).read_text(encoding="utf-8"))
x=load("research/pre-expert-maximum.json")
state=load("analysis/current-status.json")
cov=load("analysis/occurrence-coverage-v1.json")
assert x["target"]=="PRE_EXPERT_MAXIMUM"
assert len(cov["records_without_encoded_occurrences"])==15
assert state["scientific_results"]["corpus_wide_frequency"]=="BLOCKED"
assert state["scientific_results"]["cross_script_phonetic_test"]=="BLOCKED"
assert x["remaining_nonexpert_work"] and x["human_only_boundary"]
assert all("blocked_by" in i for i in x["remaining_nonexpert_work"])
print("PASS: pre-expert maximum ledger")
