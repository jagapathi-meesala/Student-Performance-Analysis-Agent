from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
manifest = yaml.safe_load((ROOT / "agent.yaml").read_text(encoding="utf-8"))

# This check mirrors the fields and constraints used by this manifest from the
# inspected OpenGAP agent-yaml.schema.json. It is deliberately not reported as
# full CLI/schema validation.
allowed = {
    "spec_version", "name", "version", "description", "author", "license",
    "model", "extends", "dependencies", "skills", "tools", "agents",
    "delegation", "runtime", "a2a", "compliance", "registries", "tags",
    "mcp_servers", "metadata",
}
unknown = set(manifest) - allowed
assert not unknown, f"unsupported root properties: {sorted(unknown)}"
assert re.fullmatch(r"^[a-z][a-z0-9-]*$", manifest["name"])
assert re.fullmatch(r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$", manifest["version"])
assert manifest["spec_version"] == "0.1.0"
assert isinstance(manifest["description"], str) and manifest["description"]
assert len(manifest.get("skills", [])) == len(set(manifest.get("skills", [])))
assert len(manifest.get("tools", [])) == len(set(manifest.get("tools", [])))
for skill in manifest.get("skills", []):
    assert re.fullmatch(r"^[a-z][a-z0-9-]*$", skill)
    assert (ROOT / "skills" / skill / "SKILL.md").exists(), skill
for tool in manifest.get("tools", []):
    assert re.fullmatch(r"^[a-z][a-z0-9-]*$", tool)
    assert (ROOT / "tools" / f"{tool}.yaml").exists(), tool
print("manifest field and resource consistency passed")
