"""Source-stratified coverage; no label equivalences or population estimates."""
import collections,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
SOURCE_ROLES={'davis-maran-prillwitz-wirghova2023':'primary_publication','vetters2011':'primary_publication','bourogiannis2024':'dependent_secondary'}
def coverage(records,occurrences):
    ids=set(records)
    if len(ids)!=len(records):raise ValueError('duplicate native record')
    seen=set();grouped=collections.defaultdict(list)
    for o in occurrences:
        if o['record_id'] not in ids or o['occurrence_id'] in seen or not o.get('locator'):
            raise ValueError('orphan, duplicate or unlocated occurrence')
        if o['source_id'] not in SOURCE_ROLES:raise ValueError('source role requires explicit review')
        seen.add(o['occurrence_id']);grouped[o['source_id']].append(o)
    return {'scope':'Committed rich-record subset only; catalogue placeholders are outside this denominator.',
            'rich_records':len(ids),'records_with_encoded_occurrences':len({o['record_id'] for o in occurrences}),
            'records_without_encoded_occurrences':sorted(ids-{o['record_id'] for o in occurrences}),
            'encoded_occurrences':len(occurrences),
            'source_strata':[{'source_id':sid,'source_role':SOURCE_ROLES[sid],
                'records':sorted({o['record_id'] for o in rows}), 'occurrences':len(rows),
                'published_labels':dict(sorted(collections.Counter(o['published_sign_label'] for o in rows).items()))}
                for sid,rows in sorted(grouped.items())],
            'sign_labels_merged':False,'witness_independence_established':False,
            'corpus_wide_frequency_allowed':False,
            'warning':'Primary publication and secondary transnumeration are separate strata; neither source count nor coverage count establishes independent witnesses or representative corpus sampling.'}
if __name__=='__main__':
    records=json.loads((R/'corpus/index.json').read_text())['records']
    occ=json.loads((R/'occurrences/occurrences.json').read_text())['occurrences']
    print(json.dumps(coverage(records,occ),indent=2)+'\n',end='')
