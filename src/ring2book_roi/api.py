from fastapi import FastAPI

from ring2book_roi import calculate_roi_summary, load_scenario_from_json

app = FastAPI(title="Ring2Book ROI Calculator API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/scenario/{scenario_name}")
def get_scenario_summary(scenario_name: str):
    scenario_path = f"scenarios/{scenario_name}.json"
    scenario = load_scenario_from_json(scenario_path)
    summary = calculate_roi_summary(scenario)
    return summary