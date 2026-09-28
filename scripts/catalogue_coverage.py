#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
c=json.loads((R/'catalogues/master.json').read_text())
n=len(c['entries']); exact=sum(x['siglum'] is not None for x in c['entries']); rich=sum(x['ingestion_status']=='rich_record_available' for x in c['entries'])
print(json.dumps({'experiment_id':'cm-catalogue-coverage-v1','state':'READY','controlled_slots':n,'exact_sigla':exact,'rich_record_marked_slots':rich,'warning':'Metrics describe catalogue-control layers, not total known-inscription completeness.'},indent=2))
