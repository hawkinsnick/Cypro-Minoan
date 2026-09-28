import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1]
J=lambda p:json.loads((R/p).read_text())
E=[];V=(R/'VERSION').read_text().strip();idx=J('corpus/index.json')
if V!='2.0.0' or idx['version']!=V or idx['record_count']!=len(idx['records']):E.append('version/index')
for rid in idx['records']:
 if J(f'corpus/inscriptions/{rid}.json').get('record_version')!=V:E.append('record:'+rid)
cat=J('catalogues/master.json');u=J('signs/unicode-14plus.json')
if cat['entry_count']!=254 or len(cat['entries'])!=254:E.append('catalogue')
if len(u['characters'])!=99:E.append('unicode')
for p in ['interchange/documents.json','interchange/occurrences.json']:
 x=J(p)
 if x['interchange_version']!='0.1' or x['script']!='Cypro-Minoan':E.append(p)
g=J('research/experiment-gates.json')
if not any(x['state']=='BLOCKED' and not x['claim_allowed'] for x in g['experiments']):E.append('gates')
if not any(x['independence_class']=='shared_upstream' for x in J('provenance/source-lineage.json')['lineages']):E.append('lineage')
if E:print('FAIL',*E,sep='\n');sys.exit(1)
print(f'OK v{V}: {idx["record_count"]} records; 254 catalogue slots; 99 Unicode characters; interchange/API/gates/lineage conformance passed.')
