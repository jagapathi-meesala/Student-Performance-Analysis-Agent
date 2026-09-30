from adapters.portable_adapter import PortableAdapter
from adapters.registry import AdapterRegistry
from core.tools import build_tool_contracts


def setup_env(monkeypatch):
    monkeypatch.setenv("STUDENT_PERFORMANCE_PASS_THRESHOLD", "70")
    monkeypatch.setenv("STUDENT_PERFORMANCE_REVIEW_THRESHOLD", "50")
    monkeypatch.setenv("STUDENT_PERFORMANCE_RISK_THRESHOLD", "40")


def test_contracts_exist():
    assert {x.name for x in build_tool_contracts()} == {"calculate-performance", "analyze-performance", "identify-risk"}


def test_portable_invocation(monkeypatch):
    setup_env(monkeypatch)
    adapter = PortableAdapter()
    result = adapter.invoke("analyze-performance", {"assessments": [{"score": 8, "max_score": 10}]})
    assert result["ok"] is True
    assert result["data"]["metrics"]["overall_percentage"] == 80.0


def test_unknown_tool():
    assert PortableAdapter().invoke("missing", {})["error"] == "unknown_tool"


def test_registry():
    registry = AdapterRegistry()
    adapter = PortableAdapter()
    registry.register("portable", adapter)
    assert registry.discover() == ["portable"]
