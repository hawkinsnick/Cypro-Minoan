"""Execute the project-specific ISO Schematron against the generated pilot."""
from pathlib import Path
from lxml import etree, isoschematron

root = Path(__file__).resolve().parents[1]
schema = etree.parse(str(root / "interchange/epidoc/pilot-integrity.sch"))
validator = isoschematron.Schematron(schema, store_report=True)
document = etree.parse(str(root / "interchange/epidoc/occurrences-pilot.xml"))
if not validator.validate(document):
    raise AssertionError(etree.tostring(validator.validation_report, encoding="unicode"))
print("PASS: project-specific ISO Schematron occurrence integrity")
