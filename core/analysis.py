from __future__ import annotations

from typing import Any, Mapping, Sequence

from core.config import PerformanceConfig


def validate_assessments(assessments: Sequence[Mapping[str, Any]]) -> None:
    if not isinstance(assessments, Sequence) or isinstance(assessments, (str, bytes)) or not assessments:
        raise ValueError("assessments must be a non-empty list")
    for index, item in enumerate(assessments):
        if not isinstance(item, Mapping):
            raise ValueError(f"assessment {index} must be an object")
        if "score" not in item or "max_score" not in item:
            raise ValueError(f"assessment {index} requires score and max_score")
        score = item["score"]
        maximum = item["max_score"]
        if isinstance(score, bool) or isinstance(maximum, bool):
            raise ValueError(f"assessment {index} scores must be numeric")
        try:
            score_f = float(score)
            max_f = float(maximum)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"assessment {index} scores must be numeric") from exc
        if max_f <= 0:
            raise ValueError(f"assessment {index} max_score must be positive")
        if score_f < 0 or score_f > max_f:
            raise ValueError(f"assessment {index} score must be between 0 and max_score")


def calculate_performance(assessments: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    validate_assessments(assessments)
    total_score = sum(float(a["score"]) for a in assessments)
    total_max = sum(float(a["max_score"]) for a in assessments)
    overall = round((total_score / total_max) * 100, 2)
    items = []
    for a in assessments:
        pct = round((float(a["score"]) / float(a["max_score"])) * 100, 2)
        items.append({"name": str(a.get("name", "assessment")), "percentage": pct})
    return {
        "total_score": round(total_score, 2),
        "total_max_score": round(total_max, 2),
        "overall_percentage": overall,
        "assessment_percentages": items,
    }


def performance_band(percentage: float, config: PerformanceConfig) -> str:
    if percentage >= config.pass_threshold:
        return "meets_pass_threshold"
    if percentage >= config.review_threshold:
        return "needs_review"
    return "below_review_threshold"


def identify_risk(percentage: float, config: PerformanceConfig) -> dict[str, Any]:
    flagged = percentage < config.risk_threshold
    return {
        "flagged": flagged,
        "rule": "overall_percentage_below_risk_threshold",
        "threshold": config.risk_threshold,
        "explanation": (
            "Overall percentage is below the configured risk threshold."
            if flagged else
            "Overall percentage is at or above the configured risk threshold."
        ),
    }
