#!/usr/bin/env python3
"""Rebuild source-attributed review dossiers; no sign or identity adjudication."""
import argparse,collections,hashlib,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
def load(root,p):return json.loads((root/p).read_text())
def refs(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if k=='source_id':yield v
            elif k=='source_ids':yield from v
            else:yield from refs(v)
    elif isinstance(x,list):
        for v in x:yield from refs(v)
def digest(root,p):return hashlib.sha256((root/p).read_bytes()).hexdigest()
def calculate(root=R):
    ch=(root/'corpus/chic-catalogue-spine.json').exists()
    bibliography=load(root,'bibliography/sources.json')
    key='id' if ch else 'source_id';sources={x[key]:x for x in bibliography}
    if len(sources)!=len(bibliography):raise ValueError('duplicate source ID')
    evidence=['bibliography/sources.json'];dossiers=[];report={'schema_version':'1.0','project':'Cretan Hieroglyphic' if ch else 'Cypro-Minoan','release':(root/'VERSION').read_text().strip(),'independent_reviews_added':0,'scientific_gates_changed':False}
    if ch:
        paths=['corpus/chic-catalogue-spine.json','corpus/critical-readings.json','corpus/context-assertions.json'];evidence+=paths
        cat=load(root,paths[0]);readings=load(root,paths[1]);context=load(root,paths[2]);ids={x['id'] for x in cat}
        rows=context['records'];rowids=[x['object_id'] for x in rows]
        if len(rowids)!=len(set(rowids)) or not set(rowids)<=ids:raise ValueError('duplicate/orphan context object')
        for row in rows:
            if row['reading_admitted'] is not False or row['independent_review'] is not False:raise ValueError('metadata promoted to reading/review')
            if row['rights']['images_included'] or row['rights']['models_included']:raise ValueError('restricted model/image included')
            if len(row['html_sha256'])!=64 or not row['source_url'].startswith('https://www.inscribercproject.com/'):raise ValueError('invalid source identity')
            fields=[a['field'] for a in row['assertions']]
            if len(fields)!=len(set(fields)):raise ValueError('duplicate source field')
            for a in row['assertions']:
                if a['source_id']!=row['source_id'] or a['source_url']!=row['source_url'] or not a.get('locator'):raise ValueError('context provenance drift')
                if a['value'] in (None,'Unknown','-') and a['status']!='source_reported_unknown':raise ValueError('unknown promoted to known')
                if a['status'] not in ('source_reported','source_reported_unknown'):raise ValueError('unsupported assertion status')
        for r in readings:
            if r['object_id'] not in ids:raise ValueError('orphan reading')
        for i,c in enumerate(cat):
            rs=[r for r in readings if r['object_id']==c['id']];cs=[r for r in rows if r['object_id']==c['id']]
            source_ids=sorted(set(refs(c))|set(refs(rs))|set(refs(cs)))
            dossiers.append({'record_id':c['id'],'series':c['series'],'native_ref':paths[0]+'#/'+str(i),'catalogue_status':c['data_status'],'source_context':cs,'source_readings':rs,'source_ids':source_ids,'missing_evidence':([] if cs else ['SOURCE_CONTEXT_NOT_ENCODED'])+([] if rs else ['SOURCE_READING_NOT_ENCODED'])+['INDEPENDENT_REVIEW_PENDING'],'identity_status':'CATALOGUE_IDENTIFIER_ONLY_NO_PHYSICAL_CERTIFICATION'})
        report.update(catalogue_entries=len(cat),dossier_count=len(dossiers),context_objects=len(rows),context_assertions=sum(len(x['assertions']) for x in rows),context_by_series={s:sum(d['series']==s and bool(d['source_context']) for d in dossiers) for s in 'HISY'},reading_objects=len({r['object_id'] for r in readings}),critical_readings=len(readings),excluded_source_pages=context['excluded_pages'],objects_without_context=[d['record_id'] for d in dossiers if not d['source_context']])
    else:
        ids=load(root,'corpus/index.json')['records'];occ=load(root,'occurrences/occurrences.json')['occurrences'];catalogue=load(root,'catalogues/master.json')['entries'];evidence+=['corpus/index.json','occurrences/occurrences.json','catalogues/master.json'];links=collections.defaultdict(list)
        for rid in sorted(ids):
            p='corpus/inscriptions/'+rid+'.json';evidence.append(p);record=load(root,p)
            if record['id']!=rid:raise ValueError('native identity mismatch')
            os=[o for o in occ if o['record_id']==rid]
            for ident in record['identifiers']:
                if 'catalogue' in ident['system'].lower():
                    try:n=int(ident['value'])
                    except (TypeError,ValueError):continue
                    links[n].append({'record_id':rid,'authority':ident['system'],'source_id':ident['source_id']})
            source_ids=sorted(set(refs(record))|set(refs(os)))
            dossiers.append({'record_id':rid,'native_ref':p,'native_sha256':digest(root,p),'object':record['object'],'find_context':record['find_context'],'dating':record['dating'],'identifiers':record['identifiers'],'classifications':record['classifications'],'assertions':record['assertions'],'source_occurrences':os,'source_ids':source_ids,'rights':record['rights'],'missing_evidence':([] if os else ['ENCODED_OCCURRENCES_ABSENT'])+([] if record['dating'] else ['DATED_ASSERTION_ABSENT'])+['INDEPENDENT_REVIEW_PENDING'],'occurrence_scope':'Partial source-attributed occurrence subset; no complete transcription inferred.'})
        slots=[{'catalogue_number':c['catalogue_number'],'authority_layer':c['authority_layer'],'siglum':c['siglum'],'ingestion_status':c['ingestion_status'],'reported_record_links':sorted(links.get(c['catalogue_number'],[]),key=lambda x:(x['record_id'],x['authority'])),'mapping_status':'SOURCE_REPORTED_LINK' if links.get(c['catalogue_number']) else 'NO_RICH_RECORD_LINK_REGISTERED'} for c in catalogue]
        report.update(controlled_catalogue_slots=len(slots),dossier_count=len(dossiers),rich_records=len(ids),records_with_occurrences=sum(bool(d['source_occurrences']) for d in dossiers),encoded_occurrences=len(occ),records_with_dating=sum(bool(d['dating']) for d in dossiers),catalogue_slot_accounting=slots,slots_with_reported_record_links=sum(bool(s['reported_record_links']) for s in slots),source_locator_limits=[{'source_id':s,'status':sources[s].get('verification_status')} for s in sorted(sources) if sources[s].get('verification_status') in ('LOCATOR_LEAD_ACCESS_FAILED','BIBLIOGRAPHY_CHECKED_VIA_LOUVRE_ARTICLE_UNINSPECTED')])
    for d in dossiers:
        missing=set(d['source_ids'])-set(sources)
        if missing:raise ValueError('orphan source references: '+d['record_id']+' '+str(sorted(missing)))
        d['sources']=[sources[s] for s in d['source_ids']]
    report['input_digests']=[{'path':p,'sha256':digest(root,p)} for p in sorted(evidence)]
    report['boundary']='Catalogue/context/occurrence coverage are separate. Source attribution is not independent verification; no phonetic, semantic or representative-population claim is authorized.'
    return {'schema_version':'1.0','project':report['project'],'release':report['release'],'dossiers':dossiers,'claim_boundary':report['boundary']},report

def markdown(bundle):
    def cell(v):
        if isinstance(v,(dict,list)):v=json.dumps(v,ensure_ascii=False)
        return str(v).replace('|','\\|').replace('\n',' ')
    lines=['# Record review dossiers','',bundle['claim_boundary'],'',
           'Source-reported metadata and partial readings remain distinct. Every dossier awaits independent review.','']
    for d in bundle['dossiers']:
        lines += ['## '+d['record_id'],'','Native evidence: ['+d['native_ref']+'](../'+d['native_ref']+')','']
        rows=[]
        if 'source_context' in d:
            for r in d['source_context']:
                for a in r['assertions']:rows.append((a['field'],a['value'],a['status'],a['source_id']+' / '+a['locator']))
            lines += ['Catalogue series: '+d['series']+'. Encoded readings: '+str(len(d['source_readings']))+'.','']
        else:
            for k,v in d['object'].items():rows.append((k,v,'native_record',d['native_ref']))
            rows.append(('find_context',d['find_context'],'source_reported',d['native_ref']))
            for a in d['dating']:rows.append((a['assertion_type'],a['value'],a['uncertainty'],str(a['provenance'])))
            lines += ['Encoded occurrences: '+str(len(d['source_occurrences']))+'; a complete transcription is not inferred.','']
        if rows:
            lines += ['| Field | Value | Status | Evidence |','|---|---|---|---|']
            lines += ['| '+' | '.join(cell(v) for v in row)+' |' for row in rows]
            lines.append('')
        lines += ['Missing evidence: '+', '.join(d['missing_evidence'])+'.','']
        for a in d['sources']:
            sid=a.get('id',a.get('source_id'));u=a.get('url')
            lines += [('- ['+sid+']('+u+')' if u else '- '+sid)+': '+a.get('title','')]
        lines.append('')
    return '\n'.join(lines)+'\n'

def validate(root=R):
    expected=calculate(root)
    for p,x in zip(['research/record-dossiers.json','analysis/context-coverage-v1.json'],expected):
        if load(root,p)!=x:raise ValueError('dossier/coverage replay drift: '+p)
    if (root/'docs/RECORD-DOSSIERS.md').read_text()!=markdown(expected[0]):raise ValueError('readable dossier replay drift')
    return {'status':'PASS','dossiers':len(expected[0]['dossiers']),'source_references_closed':True,'scientific_gates_changed':False}
def write(root=R):
    (root/'docs/RECORD-DOSSIERS.md').write_text(markdown(calculate(root)[0]))
    for p,x in zip(['research/record-dossiers.json','analysis/context-coverage-v1.json'],calculate(root)):(root/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
    if a.write:write()
    print(json.dumps(validate()))
