"""Hostile tests for source closure, metadata leakage and generated view tampering."""
import copy,json,pathlib,shutil,tempfile
from research_dossiers import calculate,validate,R
validate()
with tempfile.TemporaryDirectory() as td:
    root=pathlib.Path(td)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def reject(path,mutate):
        p=root/path;raw=p.read_bytes();x=json.loads(raw);mutate(x);p.write_text(json.dumps(x))
        try:
            try:validate(root)
            except (ValueError,KeyError):pass
            else:raise AssertionError('hostile change accepted: '+path)
        finally:p.write_bytes(raw)
    reject('bibliography/sources.json',lambda x:x.pop())
    reject('research/record-dossiers.json',lambda x:x['dossiers'].pop())
    reject('analysis/context-coverage-v1.json',lambda x:x.update(dossier_count=9999))
    if (root/'corpus/context-assertions.json').exists():
        reject('corpus/context-assertions.json',lambda x:x['records'].append(copy.deepcopy(x['records'][0])))
        reject('corpus/context-assertions.json',lambda x:x['records'][0].update(object_id='CHIC-999'))
        reject('corpus/context-assertions.json',lambda x:x['records'][0].update(reading_admitted=True))
        reject('corpus/context-assertions.json',lambda x:x['records'][0]['rights'].update(models_included=True))
        def unknown(x):
            a=next(a for r in x['records'] for a in r['assertions'] if a['status']=='source_reported_unknown');a['status']='source_reported'
        reject('corpus/context-assertions.json',unknown)
    else:
        p='corpus/inscriptions/'+json.loads((root/'corpus/index.json').read_text())['records'][0]+'.json'
        reject(p,lambda x:x['identifiers'][0].update(source_id='invented-source'))
        reject(p,lambda x:x.update(id='invented-object'))
    validate(root)
print('PASS: source closure, orphan/duplicate rejection, generated tampering and metadata/reading boundary')
