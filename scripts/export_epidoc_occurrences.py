#!/usr/bin/env python3
"""Loss-aware EpiDoc pilot exporter for Cypro-Minoan source-checked occurrences.

This exporter deliberately serializes only attested occurrence assertions. It does
not claim complete transcription, decipherment, sign equivalence, or source
independence.
"""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path
import xml.etree.ElementTree as ET

TEI = "http://www.tei-c.org/ns/1.0"
XML = "http://www.w3.org/XML/1998/namespace"
ET.register_namespace("", TEI)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "occurrences" / "occurrences.json"
OUT = ROOT / "interchange" / "epidoc" / "occurrences-pilot.xml"

def q(name: str) -> str:
    return f"{{{TEI}}}{name}"

def build() -> ET.Element:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    root = ET.Element(q("TEI"), {f"{{{XML}}}id": "CM-occurrences-pilot"})
    header = ET.SubElement(root, q("teiHeader"))
    fd = ET.SubElement(header, q("fileDesc"))
    ts = ET.SubElement(fd, q("titleStmt"))
    ET.SubElement(ts, q("title")).text = "Cypro-Minoan source-checked occurrence pilot"
    ps = ET.SubElement(fd, q("publicationStmt"))
    ET.SubElement(ps, q("p")).text = "Project-generated interchange view; consult repository rights metadata."
    sd = ET.SubElement(fd, q("sourceDesc"))
    ET.SubElement(sd, q("p")).text = (
        "Generated only from occurrences/occurrences.json. Coverage is partial and "
        "authority-specific; omission is not evidence of absence."
    )
    rev = ET.SubElement(header, q("revisionDesc"))
    ET.SubElement(rev, q("change"), {"when": "2026-10-06"}).text = (
        "Pilot loss-aware serialization; no decipherment or normalization asserted."
    )

    text = ET.SubElement(root, q("text"))
    body = ET.SubElement(text, q("body"))
    grouped = defaultdict(list)
    for occ in data["occurrences"]:
        grouped[(occ["record_id"], occ["zone_id"])].append(occ)

    for (record_id, zone_id), occurrences in sorted(grouped.items()):
        div = ET.SubElement(body, q("div"), {
            "type": "edition",
            "subtype": "partial-source-assertions",
            f"{{{XML}}}id": f"{record_id}-{zone_id}".replace("_", "-"),
        })
        ET.SubElement(div, q("head")).text = f"{record_id} / {zone_id}"
        ab = ET.SubElement(div, q("ab"), {"type": "occurrence-sequence", "ana": "#partial-coverage"})
        for occ in sorted(occurrences, key=lambda x: x["position"]):
            g = ET.SubElement(ab, q("g"), {
                "n": str(occ["position"]),
                "ref": f"urn:cypro-minoan:published-sign:{occ['source_id']}:{occ['published_sign_label']}",
                "cert": occ.get("certainty", "unknown"),
                "resp": f"#source-{occ['source_id']}",
                "ana": f"#source-role-{occ.get('source_role', 'unknown')}",
                f"{{{XML}}}id": occ["occurrence_id"],
            })
            g.text = occ["published_sign_label"]
            note = ET.SubElement(div, q("note"), {"type": "source-locator", "corresp": f"#{occ['occurrence_id']}"})
            note.text = occ["locator"]
        if "potmark" in zone_id.lower():
            div.set("ana", "#nonlinguistic-status-undetermined")
    return root

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    root = build()
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(OUT, encoding="utf-8", xml_declaration=True)
    print(OUT.relative_to(ROOT))

if __name__ == "__main__":
    main()
