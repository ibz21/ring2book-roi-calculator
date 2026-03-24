import json

from ring2book_roi.calculator import (
    calculate_missed_calls_per_month,
    calculate_roi_summary,
)
from ring2book_roi.presets import load_scenario_from_json


def load_scenario():
    return load_scenario_from_json("scenarios/plumber_base.json")


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


def test_load_electrician_scenario():
    scenario = load_scenario_from_json("scenarios/electrician_base.json")

    assert scenario.business_name == "Example Electrical Co"
    assert scenario.trade_type == "Electrical"
    assert scenario.monthly_inbound_calls == 90
    assert scenario.missed_call_rate == 0.25

def test_calculate_electrician_roi_summary():
    scenario = load_scenario_from_json("scenarios/electrician_base.json")
    summary = calculate_roi_summary(scenario)

    assert summary["missed_calls_per_month"] == 22.5
    assert summary["baseline_completed_jobs"] == 1.96
    assert summary["baseline_revenue"] == 274.43
    assert summary["assisted_completed_jobs"] == 5.423
    assert summary["assisted_revenue"] == 759.22
    assert summary["incremental_revenue"] == 484.79
    assert summary["monthly_cost"] == 330.67
    assert summary["net_monthly_gain"] == 154.13
    assert summary["roi_multiple"] == 1.47
    assert summary["setup_payback_months"] == 5.13

def test_cli_summary_uses_loader_and_calculator():
    scenario = load_scenario_from_json("scenarios/plumber_base.json")
    summary = calculate_roi_summary(scenario)

    assert summary["missed_calls_per_month"] == 36.0
    assert summary["roi_multiple"] == 2.13