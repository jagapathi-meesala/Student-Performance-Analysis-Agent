from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "EXPLAINABILITY.md").read_text(encoding="utf-8")
required = ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]
for heading in required:
    assert heading in text, heading
assert "\n## Inputs\n" not in text
assert "\n## Decision\n" not in text
assert "\n## Limits\n" not in text
for heading in required:
    start = text.index(heading) + len(heading)
    next_heading = text.find("\n## ", start)
    section = text[start: next_heading if next_heading != -1 else len(text)]
    body = section.strip()
    assert len(re.findall(r"[.!?](?:\s|$)", body)) >= 2, f"insufficient sentences under {heading}"
print("documentation structure passed")
