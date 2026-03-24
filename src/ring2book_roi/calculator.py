from ring2book_roi.models import RoiScenarioInput


def calculate_missed_calls_per_month(scenario: RoiScenarioInput) -> float:
    """Return the estimated number of missed calls per month."""
    return scenario.monthly_inbound_calls * scenario.missed_call_rate

def calculate_baseline_completed_jobs(scenario: RoiScenarioInput) -> float:
    """Return the estimated number of completed jobs recovered in the current state."""
    missed_calls = calculate_missed_calls_per_month(scenario)
    return (
        missed_calls
        * scenario.current_recovery_rate
        * scenario.current_booking_rate
        * scenario.current_completion_rate
    )

def calculate_baseline_revenue(scenario: RoiScenarioInput) -> float:
    """Return the estimated monthly revenue recovered in the current state."""
    baseline_completed_jobs = calculate_baseline_completed_jobs(scenario)
    return baseline_completed_jobs * scenario.average_job_value

def calculate_assisted_completed_jobs(scenario: RoiScenarioInput) -> float:
    """Return the estimated number of completed jobs with Ring2Book."""
    missed_calls = calculate_missed_calls_per_month(scenario)
    return (
        missed_calls
        * scenario.assisted_contact_rate
        * scenario.assisted_engagement_rate
        * scenario.assisted_qualification_rate
        * scenario.assisted_booking_rate
        * scenario.assisted_completion_rate
    )

def calculate_assisted_revenue(scenario: RoiScenarioInput) -> float:
    """Return the estimated monthly revenue recovered with Ring2Book."""
    assisted_completed_jobs = calculate_assisted_completed_jobs(scenario)
    return assisted_completed_jobs * scenario.average_job_value

def calculate_incremental_revenue(scenario: RoiScenarioInput) -> float:
    """Return the additional monthly revenue recovered with Ring2Book."""
    assisted_revenue = calculate_assisted_revenue(scenario)
    baseline_revenue = calculate_baseline_revenue(scenario)
    return assisted_revenue - baseline_revenue

def calculate_monthly_cost(scenario: RoiScenarioInput) -> float:
    """Return the monthly cost used in the ROI model."""
    amortised_setup_fee = scenario.setup_fee / scenario.setup_amortisation_months
    return scenario.monthly_plan_cost + amortised_setup_fee

def calculate_net_monthly_gain(scenario: RoiScenarioInput) -> float:
    """Return the net monthly gain after subtracting monthly cost."""
    incremental_revenue = calculate_incremental_revenue(scenario)
    monthly_cost = calculate_monthly_cost(scenario)
    return incremental_revenue - monthly_cost

def calculate_roi_multiple(scenario: RoiScenarioInput) -> float:
    """Return the ROI multiple based on incremental revenue and monthly cost."""
    incremental_revenue = calculate_incremental_revenue(scenario)
    monthly_cost = calculate_monthly_cost(scenario)
    return incremental_revenue / monthly_cost

def calculate_setup_payback_months(scenario: RoiScenarioInput) -> float:
    """Return how many months it takes to recover the setup fee from net monthly gain."""
    net_monthly_gain = calculate_net_monthly_gain(scenario)
    return scenario.setup_fee / net_monthly_gain


def calculate_roi_summary(scenario: RoiScenarioInput) -> dict:
    """Return the main calculator outputs in one summary object."""
    return {
        "missed_calls_per_month": round(calculate_missed_calls_per_month(scenario), 2),
        "baseline_completed_jobs": round(calculate_baseline_completed_jobs(scenario), 3),
        "baseline_revenue": round(calculate_baseline_revenue(scenario), 2),
        "assisted_completed_jobs": round(calculate_assisted_completed_jobs(scenario), 3),
        "assisted_revenue": round(calculate_assisted_revenue(scenario), 2),
        "incremental_revenue": round(calculate_incremental_revenue(scenario), 2),
        "monthly_cost": round(calculate_monthly_cost(scenario), 2),
        "net_monthly_gain": round(calculate_net_monthly_gain(scenario), 2),
        "roi_multiple": round(calculate_roi_multiple(scenario), 2),
        "setup_payback_months": round(calculate_setup_payback_months(scenario), 2),
    }