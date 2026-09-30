from pathlib import Path


def test_explainability_headings():
    text = Path("EXPLAINABILITY.md").read_text()
    assert "## Inputs and Data Sources" in text
    assert "## Decision and Reasoning" in text
    assert "## Limits and Constraints" in text
    assert "\n## Inputs\n" not in text
    assert "\n## Decision\n" not in text
    assert "\n## Limits\n" not in text
