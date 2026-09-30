from adapters.claude_code_adapter import claude_code_Adapter
from adapters.crewai_adapter import crewai_Adapter
from adapters.lyzr_adapter import lyzr_Adapter
from adapters.openai_adapter import openai_Adapter


def test_adapter_boundaries_are_framework_independent():
    for cls in (openai_Adapter, crewai_Adapter, claude_code_Adapter, lyzr_Adapter):
        adapter = cls()
        assert adapter.list_tools() == ["analyze-performance", "calculate-performance", "identify-risk"]
