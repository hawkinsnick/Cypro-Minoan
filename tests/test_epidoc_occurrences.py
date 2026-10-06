#!/usr/bin/env python3
"""Invariant tests for the loss-aware EpiDoc pilot."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cm_epidoc", ROOT / "scripts" / "export_epidoc_occurrences.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

root = mod.build()
xml = __import__("xml.etree.ElementTree", fromlist=["ElementTree"]).tostring(root, encoding="unicode")
assert "partial-source-assertions" in xml
assert "#partial-coverage" in xml
assert "source-role-dependent_secondary" in xml
assert "CMOCC-TIRY245-H2-M1" in xml
assert "nonlinguistic-status-undetermined" in xml
assert "CM025" in xml and "CM087" in xml
for forbidden in ("phonetic", "deciphered", "complete-transcription"):
    assert forbidden not in xml.lower()
print("EpiDoc pilot invariants: PASS")
