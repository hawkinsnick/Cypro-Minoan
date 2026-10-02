#!/usr/bin/env python3
import hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];A=R/"ai-skill";errors=[]
d=json.loads((A/"generated"/"research-bundle-index.json").read_text())
m=json.loads((A/"manifest.json").read_text())
p=json.loads((A/"references"/"authority-profile.json").read_text())
s=(A/"SKILL.md").read_text()
x=re.search(r"^version:\s*([^\s]+)",s,re.M);sv=x.group(1) if x else None
if sv!=m.get("skill_version"):errors.append("skill manifest mismatch")
if d.get("skill_version")!=m.get("skill_version"):errors.append("bundle manifest mismatch")
if d.get("schema_version")!=m.get("bundle_schema"):errors.append("bundle schema mismatch")
idx={a.get("path"):a for a in d.get("artifacts",[])}
for q in p.get("required_authorities",[]):
 f=R/q["path"]
 if not f.is_file():errors.append("missing authority "+q["path"]);continue
 a=idx.get(q["path"])
 if not a:errors.append("authority not indexed "+q["path"]);continue
 if a.get("sha256")!=hashlib.sha256(f.read_bytes()).hexdigest():errors.append("authority hash mismatch "+q["path"])
if errors:print("\n".join(errors));sys.exit(1)
print("Cypro-Minoan AI integration validation PASS")
