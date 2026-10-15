#!/usr/bin/env python3
"""Build a vendor-neutral, provenance-aware AI research bundle from canonical repo artifacts."""
import csv, hashlib, json, os, subprocess
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"ai-skill"/"generated"; OUT.mkdir(parents=True,exist_ok=True)
sha=os.environ.get("SOURCE_COMMIT") or subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
CANDIDATES=[('native_evidence_profile', 'research/evidence-query-profile.json'), ('native_evidence_coverage', 'analysis/evidence-query-coverage.json'), ('native_evidence_query', 'scripts/evidence_query.py'), ('native_evidence_query_tests', 'scripts/test_native_evidence_query.py'), ('native_evidence_guide', 'docs/EVIDENCE-AND-ALTERNATIVES.md')]+[('CM209_source_check', 'research/source-check-CMOC-0209-2026-10-14.json'), ('CM209_source_check', 'docs/CMOC-0209-SOURCE-CHECK.md'), ('CM209_source_check', 'scripts/validate_CM209_20261014.py')]+[('finite_source_growth', 'research/source-growth-2026-10-14.json'), ('finite_source_growth', 'docs/SOURCE-GROWTH-2026-10-14.md'), ('finite_source_growth', 'scripts/validate_growth_20261014.py')]+[('source_growth', 'research/louvre-object-concordance.json'), ('source_growth', 'research/tiryns-clay-ball-primary-context.json'), ('source_growth', 'analysis/source-growth-2026-10-12.json'), ('source_growth', 'docs/SOURCE-GROWTH-2026-10-12.md'), ('source_growth', 'scripts/source_growth.py')]+[
 ("cross_corpus_dependencies","research/cross-corpus-dependencies.json"),("sync_publication_guard","ai-skill/scripts/publish_sync.py"),("ai_integrity_guide","docs/AI-INTEGRITY.md"),
 ("qualified_assertions","research/qualified-assertion-views.json"),
 ("existing_assertion_check","research/donnelly-existing-assertion-check.json"),
 ("reference_reconciliation","research/reference-reconciliation-v2.json"),("identity_reconciliation","research/identity-reconciliation-v2.json"),
 ("source_expansion","research/source-check-2026-10-11.json"),("source_reconciliation","research/source-reconciliation.json"),("coverage_denominators","research/coverage-denominators.json"),("met_api_331665","research/source-metadata/met-331665.json"),("met_api_321391","research/source-metadata/met-321391.json"),("met_api_240899","research/source-metadata/met-240899.json"),("met_api_243938","research/source-metadata/met-243938.json"),("uncovered_record_controls","research/uncovered-record-review-controls.json"),("met_open_image_controls","research/met-open-image-controls.json"),("uncovered_record_guide","docs/UNCOVERED-RECORD-REVIEW.md"),("catalogue_concordance","catalogues/source-located-concordance.json"),("catalogue_master","catalogues/master.json"),("catalogue_mapping_audit","analysis/catalogue-mapping-audit.json"),("catalogue_mapping_guide","docs/CATALOGUE-CONCORDANCE.md"),("upstream_epidoc_validation","analysis/upstream-epidoc-validation.json"),("upstream_epidoc_pins","interchange/epidoc/upstream-pins.json"),("epidoc_interoperability_audit","analysis/epidoc-interoperability-audit.json"),("epidoc_pilot_guide","docs/EPIDOC-PILOT.md")]+[
 ("readable_dossiers","docs/RECORD-DOSSIERS.md"),
 ("record_dossiers","research/record-dossiers.json"),("context_coverage","analysis/context-coverage-v1.json"),("context_assertions","corpus/context-assertions.json"),("bibliography","bibliography/sources.json"),("context_guide","docs/CONTEXT-AND-DOSSIERS.md"),
 ("current_status","analysis/current-status.json"),("source_inspection","research/source-inspection-2026-10-02.json"),("experiment_gates","research/experiment-gates.json"),("occurrence_coverage","analysis/occurrence-coverage-v1.json"),("coverage_delta","research/coverage-delta-register.json"),("pre_expert_maximum","research/pre-expert-maximum.json"),("pre_expert_source_exhaustion","research/pre-expert-source-exhaustion.json"),("occurrences","occurrences/occurrences.json"),("audit","exports/audit.json"),
 ("coverage","data/coverage.json"),("claims","release/CLAIM-REGISTRY.csv"),
 ("corpus_json","exports/corpus.json"),("corpus_jsonl","exports/corpus.jsonl"),
 ("greek_subset","exports/greek-subset.json"),("eteocypriot_components","exports/eteocypriot-components.json"),
 ("rights_matrix","DATA-LICENSE-MATRIX.md"),("rights","docs/RIGHTS.md"),
 ("rights_and_licensing","docs/RIGHTS-AND-LICENSING.md"),("notice","NOTICE"),("third_party","THIRD-PARTY-NOTICES.md")
]
artifacts=[]
for role,rel in CANDIDATES:
 p=ROOT/rel
 if p.is_file():
  b=p.read_bytes(); artifacts.append({"role":role,"path":rel,"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)})
bundle={"schema_version":"0.3.1","skill_version":"0.3.1","source_commit":sha,
 "generated_at_utc":datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
 "canonical_repository":True,
 "contract":{"corpus_is_authoritative":True,"missing_means_unknown":True,"cross_corpus_equivalence_requires_explicit_evidence":True,
 "preserve_uncertainty":True,"preserve_source_independence":True,"preserve_rights":True},
 "artifacts":artifacts}
(OUT/"research-bundle-index.json").write_text(json.dumps(bundle,indent=2)+"\n",encoding="utf-8")
(OUT/"source-state.json").write_text(json.dumps({"schema_version":"1.0","source_commit":sha,"skill_version":"0.3.1","bundle_index":"ai-skill/generated/research-bundle-index.json"},indent=2)+"\n",encoding="utf-8")
print(f"Indexed {len(artifacts)} canonical artifacts at {sha}")
