import json
from pathlib import Path

from jsonschema import validate

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schemas"


def load_schema(name):
    with open(SCHEMA_DIR / name, encoding="utf-8") as f:
        return json.load(f)


def assert_matches_schema(payload, schema_name):
    """Raise jsonschema.ValidationError if payload does not match the schema."""
    validate(instance=payload, schema=load_schema(schema_name))
