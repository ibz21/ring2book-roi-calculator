import json

from ring2book_roi.calculator import (
    calculate_missed_calls_per_month,
    calculate_roi_summary,
)
from ring2book_roi.models import RoiScenarioInput


def load_scenario():
    with open("scenarios/plumber_base.json", "r") as file:
        data = json.load(file)
    return RoiScenarioInput(**data)


def test_calculate_missed_calls_per_month():
    scenario = load_scenario()
    result = calculate_missed_calls_per_month(scenario)
    assert result == 36.0


def test_calculate_roi_summary():
    scenario = load_scenario()
    summary = calculate_roi_summary(scenario)

    assert summary["missed_calls_per_month"] == 36.0
    assert summary["baseline_completed_jobs"] == 3.672
    assert summary["baseline_revenue"] == 403.92
    assert summary["assisted_completed_jobs"] == 10.073
    assert summary["assisted_revenue"] == 1108.0
    assert summary["incremental_revenue"] == 704.08
    assert summary["monthly_cost"] == 330.67
    assert summary["net_monthly_gain"] == 373.42
    assert summary["roi_multiple"] == 2.13
    assert summary["setup_payback_months"] == 2.12