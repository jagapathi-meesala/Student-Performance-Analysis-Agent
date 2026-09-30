from __future__ import annotations

from typing import Any, Mapping

from contracts.tool_contract import ToolContract
from core.analysis import calculate_performance, identify_risk, performance_band
from core.config import load_config


def calculate_performance_tool(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    return {"ok": True, "data": calculate_performance(payload["assessments"])}


def analyze_performance_tool(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    config = load_config()
    metrics = calculate_performance(payload["assessments"])
    band = performance_band(metrics["overall_percentage"], config)
    return {
        "ok": True,
        "data": {
            "metrics": metrics,
            "performance_band": band,
            "basis": "weighted by supplied maximum marks",
        },
    }


def identify_risk_tool(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    config = load_config()
    metrics = calculate_performance(payload["assessments"])
    return {"ok": True, "data": identify_risk(metrics["overall_percentage"], config)}


def build_tool_contracts() -> list[ToolContract]:
    common_schema = {
        "type": "object",
        "required": ["assessments"],
        "properties": {
            "assessments": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": ["score", "max_score"],
                    "properties": {
                        "name": {"type": "string"},
                        "score": {"type": "number", "minimum": 0},
                        "max_score": {"type": "number", "exclusiveMinimum": 0},
                    },
                    "additionalProperties": False,
                },
            }
        },
        "additionalProperties": False,
    }
    return [
        ToolContract("calculate-performance", "Calculate weighted academic performance metrics.", common_schema, calculate_performance_tool),
        ToolContract("analyze-performance", "Calculate metrics and assign a configured performance band.", common_schema, analyze_performance_tool),
        ToolContract("identify-risk", "Apply the configured rule-based performance risk threshold.", common_schema, identify_risk_tool),
    ]
