import os

import pytest

from core.analysis import calculate_performance, identify_risk, performance_band
from core.config import load_config


def cfg(monkeypatch):
    monkeypatch.setenv("STUDENT_PERFORMANCE_PASS_THRESHOLD", "70")
    monkeypatch.setenv("STUDENT_PERFORMANCE_REVIEW_THRESHOLD", "50")
    monkeypatch.setenv("STUDENT_PERFORMANCE_RISK_THRESHOLD", "40")
    return load_config()


def test_weighted_metrics():
    result = calculate_performance([{"name": "A", "score": 18, "max_score": 20}, {"name": "B", "score": 32, "max_score": 40}])
    assert result["overall_percentage"] == 83.33


def test_band(monkeypatch):
    config = cfg(monkeypatch)
    assert performance_band(75, config) == "meets_pass_threshold"
    assert performance_band(60, config) == "needs_review"
    assert performance_band(30, config) == "below_review_threshold"


def test_risk(monkeypatch):
    config = cfg(monkeypatch)
    assert identify_risk(39.9, config)["flagged"] is True
    assert identify_risk(40, config)["flagged"] is False

@pytest.mark.parametrize("bad", [[], [{"score": 1}], [{"score": -1, "max_score": 10}], [{"score": 11, "max_score": 10}], [{"score": 1, "max_score": 0}]])
def test_invalid_assessments(bad):
    with pytest.raises(ValueError):
        calculate_performance(bad)
