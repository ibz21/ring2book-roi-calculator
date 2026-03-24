
Then paste this into `docs/calculator-spec.md` and save.

```md
# Calculator Spec

## Core question

For a given trades business, how much revenue is currently lost from missed calls, and how much of that could Ring2Book recover each month?

## Modelling approach

The calculator compares two states:

### 1. Baseline state
What happens today without Ring2Book.

### 2. Assisted state
What happens with Ring2Book follow-up and booking workflow.

The result is the incremental uplift between those two states.

## Core assumptions

- The trigger is a missed inbound call
- Not every missed call becomes a booked job
- Some missed calls are already recovered manually today
- Ring2Book increases the recovery rate through faster follow-up and structured booking flow
- Deposits can improve show or completion rate, but should not be double-counted as extra revenue

## Minimum inputs for v1

### Prospect inputs
- business_name
- trade_type
- monthly_inbound_calls
- missed_call_rate
- average_job_value

### Current-state inputs
- current_recovery_rate
- current_booking_rate
- current_completion_rate

### Ring2Book assisted-state inputs
- assisted_contact_rate
- assisted_engagement_rate
- assisted_qualification_rate
- assisted_booking_rate
- assisted_completion_rate

### Commercial inputs
- monthly_plan_cost
- setup_fee
- setup_amortisation_months

## Core outputs

- missed_calls_per_month
- baseline_completed_jobs
- baseline_revenue
- assisted_completed_jobs
- assisted_revenue
- incremental_completed_jobs
- incremental_revenue
- monthly_cost
- net_monthly_gain
- roi_multiple
- setup_payback_months

## Example formulas

missed_calls = monthly_inbound_calls * missed_call_rate

baseline_completed_jobs =
missed_calls
* current_recovery_rate
* current_booking_rate
* current_completion_rate

baseline_revenue =
baseline_completed_jobs * average_job_value

assisted_completed_jobs =
missed_calls
* assisted_contact_rate
* assisted_engagement_rate
* assisted_qualification_rate
* assisted_booking_rate
* assisted_completion_rate

assisted_revenue =
assisted_completed_jobs * average_job_value

incremental_completed_jobs =
assisted_completed_jobs - baseline_completed_jobs

incremental_revenue =
assisted_revenue - baseline_revenue

monthly_cost =
monthly_plan_cost + (setup_fee / setup_amortisation_months)

net_monthly_gain =
incremental_revenue - monthly_cost

roi_multiple =
incremental_revenue / monthly_cost

setup_payback_months =
setup_fee / net_monthly_gain

## Notes for future versions

Future versions may add:
- emergency vs non-emergency job mix
- WhatsApp vs SMS fallback assumptions
- deposits on or off
- seasonality
- confidence scoring
- scenario comparison