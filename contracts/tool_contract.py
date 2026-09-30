from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Mapping


@dataclass(frozen=True)
class ToolContract:
    name: str
    purpose: str
    input_schema: Mapping[str, Any]
    execute: Callable[[Mapping[str, Any]], Mapping[str, Any]]

    def validate(self, payload: Mapping[str, Any]) -> None:
        if not isinstance(payload, Mapping):
            raise TypeError("tool input must be an object")

    def run(self, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        self.validate(payload)
        return self.execute(payload)
