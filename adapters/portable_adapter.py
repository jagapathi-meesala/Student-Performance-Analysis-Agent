from __future__ import annotations

from typing import Any, Mapping

from core.tools import build_tool_contracts


class PortableAdapter:
    """Framework-independent invocation boundary."""

    def __init__(self) -> None:
        self._tools = {tool.name: tool for tool in build_tool_contracts()}

    def list_tools(self) -> list[str]:
        return sorted(self._tools)

    def invoke(self, tool_name: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        if tool_name not in self._tools:
            return {"ok": False, "error": "unknown_tool"}
        try:
            return self._tools[tool_name].run(payload)
        except (KeyError, TypeError, ValueError, RuntimeError) as exc:
            return {"ok": False, "error": "invalid_request", "message": str(exc)}
