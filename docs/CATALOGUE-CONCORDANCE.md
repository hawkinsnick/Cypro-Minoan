# Source-located catalogue reconciliation

On 2026-10-11 the project visually inspected Valério’s 2016 thesis concordance on PDF pages 25–27 (unnumbered front matter). The source is located by persistent handle, exact download URL, byte length and SHA-256 in `catalogues/source-located-concordance.json`. Only factual identifier pairs and provenance are redistributed. Access is not a grant to redistribute images, prose or critical transcriptions.

All 253 table rows agree with the 67 previously mapped entries in the same range. The 186 former number-only entries are filled from this table; slot 254 retains its distinct Valério 2017 attribution. Authority layers remain separate: HoChyMin 1–217, CMI 218–244, further addenda 245–253. The current controlled register has 254 source-attributed sigla and no number-only slots. This is a bounded register, not a terminal world-corpus count.

Exact source labels remain available, including asterisks at 19 and 73 and uncertain site `ENKO?` at 169. Native identifier strings exclude the editorial asterisk, which is stored separately with meaning `NOT_ADJUDICATED`; no uncertainty is silently resolved. Existing later asterisks are also retained in the concordance control.

Run `python scripts/catalogue_concordance.py` for exact replay, or pass `--source-pdf /path/to/download.pdf` to additionally verify the original PDF digest. Automated replay checks the committed source-qualified joins, not the scholar’s readings. The source table depends on earlier editions and supplies no independent witness.

The population remains 21 rich records and 12 encoded source-attributed occurrences on six records; 15 rich records still lack encoded occurrences. No sign readings, phonetic values, physical identity certifications or expert verdicts are added. The corpus-wide frequency and cross-script phonetic gates remain blocked.
