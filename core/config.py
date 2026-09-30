from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class PerformanceConfig:
    pass_threshold: float
    review_threshold: float
    risk_threshold: float


def _required_percentage(name: str) -> float:
    raw = os.getenv(name)
    if raw is None or not raw.strip():
        raise RuntimeError(f"Required environment variable is missing: {name}")
    try:
        value = float(raw)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable {name} must be numeric") from exc
    if not 0 <= value <= 100:
        raise RuntimeError(f"Environment variable {name} must be between 0 and 100")
    return value


def load_config() -> PerformanceConfig:
    config = PerformanceConfig(
        pass_threshold=_required_percentage("STUDENT_PERFORMANCE_PASS_THRESHOLD"),
        review_threshold=_required_percentage("STUDENT_PERFORMANCE_REVIEW_THRESHOLD"),
        risk_threshold=_required_percentage("STUDENT_PERFORMANCE_RISK_THRESHOLD"),
    )
    if config.pass_threshold < config.review_threshold:
        raise RuntimeError("STUDENT_PERFORMANCE_PASS_THRESHOLD must be >= STUDENT_PERFORMANCE_REVIEW_THRESHOLD")
    if config.review_threshold < config.risk_threshold:
        raise RuntimeError("STUDENT_PERFORMANCE_REVIEW_THRESHOLD must be >= STUDENT_PERFORMANCE_RISK_THRESHOLD")
    return config
