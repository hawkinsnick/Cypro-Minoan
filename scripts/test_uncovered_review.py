import json,tempfile,shutil
from pathlib import Path
from validate_uncovered_review import ROOT,validate
validate()
with tempfile.TemporaryDirectory() as td:
 root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
 def reject(path,mutate):
  p=root/path;b=p.read_bytes();x=json.loads(b);mutate(x);p.write_text(json.dumps(x))
  try:
   try:validate(root)
   except (ValueError,KeyError):pass
   else:raise AssertionError('hostile source/review mutation accepted')
  finally:p.write_bytes(b)
 reject('research/uncovered-record-review-controls.json',lambda x:x['items'].pop())
 reject('research/uncovered-record-review-controls.json',lambda x:x['items'][0].update(decision='ACCEPTED'))
 reject('research/met-open-image-controls.json',lambda x:x['images'][0].update(image_is_independent_witness=True))
 reject('research/met-open-image-controls.json',lambda x:x['objects'][0].update(is_public_domain=False))
 reject('research/met-open-image-controls.json',lambda x:x['images'][0].update(url='https://example.org/invented.jpg'))
 reject('research/uncovered-record-review-controls.json',lambda x:x['summary'].update(expert_reviews_completed=1))
 reject('research/uncovered-record-review-controls.json',lambda x:x['items'][0].update(status='EXPERT_VALIDATED'))
 validate(root)
print('PASS: seven adversarial source/rights/review controls')
