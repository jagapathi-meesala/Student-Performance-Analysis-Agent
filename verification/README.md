# Verification

`validate_manifest.py` validates `agent.yaml` against an exact snapshot fetched from the current OpenGAP `agent-yaml.schema.json` during project construction and verifies that every declared skill and tool exists.

`check_docs.py` verifies the parser-sensitive EXPLAINABILITY.md headings and prevents conflicting exact root headings.

The repository does not claim `opengap validate` unless that CLI is actually available and executed.
