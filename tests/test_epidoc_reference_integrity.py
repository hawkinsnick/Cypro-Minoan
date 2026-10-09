"""Check local XML references and source authority declarations in the EpiDoc pilot.

This is an integrity gate, not an EpiDoc Schematron conformance claim.
"""
from pathlib import Path
from collections import Counter
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "interchange/epidoc/occurrences-pilot.xml"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"
TEI = "{http://www.tei-c.org/ns/1.0}"

def check(path=PILOT):
    root = ET.parse(path).getroot()
    ids = [node.attrib[XML_ID] for node in root.iter() if XML_ID in node.attrib]
    duplicates = sorted(k for k, n in Counter(ids).items() if n > 1)
    errors = [f"duplicate xml:id: {x}" for x in duplicates]
    known = set(ids)
    occurrence_ids = set()
    locator_targets = set()
    for node in root.iter():
        tag = node.tag
        if tag == TEI + "g":
            oid = node.get(XML_ID)
            if not oid:
                errors.append("sign occurrence lacks xml:id")
            else:
                occurrence_ids.add(oid)
            ref = node.get("ref", "")
            if not ref.startswith("urn:cypro-minoan:published-sign:"):
                errors.append(f"{oid}: sign ref is not source-qualified")
            if not node.get("resp", "").startswith("#source-"):
                errors.append(f"{oid}: source authority not explicitly qualified")
        for attr in ("corresp", "target"):
            for token in node.get(attr, "").split():
                if token.startswith("#") and token[1:] not in known:
                    errors.append(f"unresolved {attr} target: {token}")
        if tag == TEI + "note" and node.get("type") == "source-locator":
            for token in node.get("corresp", "").split():
                if token.startswith("#"):
                    locator_targets.add(token[1:])
    for oid in sorted(occurrence_ids - locator_targets):
        errors.append(f"occurrence lacks source locator: {oid}")
    for div in root.iter(TEI + "div"):
        if div.get("type") == "edition":
            if div.get("subtype") != "partial-source-assertions":
                errors.append(f"{div.get(XML_ID)}: unqualified edition scope")
            if not any("#partial-coverage" in ab.get("ana", "").split() for ab in div.iter(TEI + "ab")):
                errors.append(f"{div.get(XML_ID)}: missing partial-coverage marker")
    if errors:
        raise AssertionError("\n".join(errors))
    print(f"PASS: {len(occurrence_ids)} source-qualified occurrences; {len(locator_targets)} source locators; local references resolved")

if __name__ == "__main__":
    check()
