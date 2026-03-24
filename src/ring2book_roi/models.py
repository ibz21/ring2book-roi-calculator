from pydantic import BaseModel, Field


class RoiScenarioInput(BaseModel):
    """Validated input schema for a single ROI calculator scenario."""

    business_name: str = Field(..., min_length=1)
    trade_type: str = Field(..., min_length=1)

    monthly_inbound_calls: int = Field(..., gt=0)
    missed_call_rate: float = Field(..., ge=0, le=1)
    average_job_value: float = Field(..., gt=0)

    current_recovery_rate: float = Field(..., ge=0, le=1)
    current_booking_rate: float = Field(..., ge=0, le=1)
    current_completion_rate: float = Field(..., ge=0, le=1)

    assisted_contact_rate: float = Field(..., ge=0, le=1)
    assisted_engagement_rate: float = Field(..., ge=0, le=1)
    assisted_qualification_rate: float = Field(..., ge=0, le=1)
    assisted_booking_rate: float = Field(..., ge=0, le=1)
    assisted_completion_rate: float = Field(..., ge=0, le=1)

    monthly_plan_cost: float = Field(..., ge=0)
    setup_fee: float = Field(..., ge=0)
    setup_amortisation_months: int = Field(..., ge=1)

    model_config = {
        "extra": "forbid"
    }