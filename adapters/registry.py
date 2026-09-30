from __future__ import annotations

from adapters.portable_adapter import PortableAdapter


class AdapterRegistry:
    def __init__(self) -> None:
        self._adapters: dict[str, PortableAdapter] = {}

    def register(self, name: str, adapter: PortableAdapter) -> None:
        if not name or not name.strip():
            raise ValueError("adapter name is required")
        if name in self._adapters:
            raise ValueError(f"adapter already registered: {name}")
        self._adapters[name] = adapter

    def discover(self) -> list[str]:
        return sorted(self._adapters)

    def get(self, name: str) -> PortableAdapter:
        return self._adapters[name]
