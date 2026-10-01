# Cypro-Minoan Open Corpus

## Current status — 5.2.8

21 rich records and 9 source-checked occurrences. Three clay-ball occurrences carry primary-publication locators. Corpus-wide frequency and cross-script phonetic claims remain blocked.

Family contract 1.2 aligns all five projects with [Phaistos Disc 1.6.0](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v1.6.0). The shared readiness report preserves native sampling units, source rights and blocked linguistic controls. It authorizes no pooling or linguistic relationship claim. See [`research/family-readiness-v1.json`](research/family-readiness-v1.json).

The authoritative current gate summary is [`analysis/current-status.json`](analysis/current-status.json). Historical release reports below retain their original versions and claims.

Validate this checkout with:

```sh
python -m pip install -r requirements-validation.txt
python scripts/validate_current_state.py
python scripts/test_current_state.py
```


**Version 5.0.0 — evidence graph and question-specific research readiness**

The corpus records evidence; it does not encode a decipherment.

5.0 links the mature 4.x reproducibility platform to an auditable evidence graph, immutable release-scoped dataset snapshots, question-specific readiness profiles, explicit witness-independence rules, representation-level rights controls, and positive/negative conformance tests.

Current evidence remains deliberately bounded: 254 controlled catalogue slots; 68 exact sigla; 21 rich records; 3 source-verified occurrences; 2 explicit witness assertions; 99 Unicode interoperability characters; no project-populated palaeographic variants. These are separate dimensions, not one completeness score.

Catalogue-structure research is READY. Descriptions of the explicitly encoded occurrence subset are READY_SCOPED. Corpus-wide sign-frequency inference and cross-script phonetic inference remain BLOCKED.

Native CM evidence remains authoritative. Interchange, evidence graphs and shared-core machinery may expose it but may not redefine it.


### Evidence progress in 5.2.8

Adds replayable source-stratified occurrence coverage: 9 encoded occurrences on 3 of 21 rich records, comprising 6 primary-publication and 3 dependent-secondary occurrences. Published labels remain separate. Whole-corpus frequencies and independent-witness claims remain blocked.

The shared family report now targets the Disc [2.0.0-rc.2 prerelease](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v2.0.0-rc.2). Final independently reviewed Disc 2.0 remains blocked; compatibility does not confer linguistic equivalence or independent review. Native evidence and this repository’s release version are unchanged.

### Research evidence workbench 1.0

Download the research workbench ZIP, extract it, and open [workbench/evidence.html](workbench/evidence.html). It includes searchable pinned evidence, coverage definitions and unverified inspection-note export. See the [reading and review guide](research/workbench-guide.md). This engineering milestone grants no independent epigraphic acceptance.

### Research workbench 1.1

Download the [research workbench 1.1 package](https://github.com/hawkinsnick/Cypro-Minoan/releases/tag/research-workbench-v1.1.0), extract it, and open `workbench/evidence.html`. It adds snapshot-bound inspection collections and includes the immutable release correction tracker. The Disc explorer also presents readable scenario comparisons. This engineering release grants no scientific acceptance.
