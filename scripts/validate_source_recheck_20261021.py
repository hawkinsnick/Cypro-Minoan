#!/usr/bin/env python3
"""Replay the bounded documentary comparison without acquiring/reproducing a PDF."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate(root=ROOT):
    r=json.loads((root/'research/source-recheck-2026-10-21.json').read_text())
    raw=(root/r['native_path']).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=r['native_path_sha256']:raise ValueError('occurrence source changed; recheck required')
    native={x['occurrence_id']:x for x in json.loads(raw)['occurrences']}
    for a in r['assertions']:
        x=native[a['occurrence_id']]
        if x['record_id']!=r['record_id'] or x['source_id']!=r['source_id'] or x['position']!=a['position'] or x['published_sign_label']!=a['recorded_source_label']:raise ValueError('documentary assertion drift')
    if r['external_specialist_review'] or r['primary_object_inspected'] or r['new_independent_witnesses']!=0:raise ValueError('unsupported acceptance upgrade')
    return {'status':'PASS_BOUNDED_DOCUMENTARY_RECHECK','occurrences':len(r['assertions']),'expert_acceptance':False}
if __name__=='__main__':print(json.dumps(validate()))
