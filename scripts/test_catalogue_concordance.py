"""Reject false joins, erased qualifiers and claims of independent/physical review."""
import copy,json,tempfile,shutil
from pathlib import Path
from catalogue_concordance import ROOT,validate
validate()
with tempfile.TemporaryDirectory() as td:
 root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
 def reject(path,mutation):
  p=root/path;raw=p.read_bytes();x=json.loads(raw);mutation(x);p.write_text(json.dumps(x))
  try:
   try:validate(root)
   except (ValueError,KeyError):pass
   else:raise AssertionError('hostile mutation accepted')
  finally:p.write_bytes(raw)
 reject('catalogues/master.json',lambda x:x['entries'][0].update(siglum='ENKO invented 999'))
 reject('catalogues/source-located-concordance.json',lambda x:x['rows'][18].update(source_label='ENKO Abou 016bis'))
 reject('catalogues/source-located-concordance.json',lambda x:x['rows'][168].update(source_label='ENKO Mins 002'))
 reject('catalogues/source-located-concordance.json',lambda x:x['rows'][0].update(independent_witness=True))
 reject('catalogues/source-located-concordance.json',lambda x:x.update(expert_validation_granted=True))
 reject('catalogues/source-located-concordance.json',lambda x:x['rows'].pop())
 reject('catalogues/master.json',lambda x:x['entries'][-1].update(source_id='valerio2016thesis'))
 validate(root)
print('PASS: mapping replay and seven adversarial provenance/uncertainty/coverage checks')
