import json

from ring2book_roi.models import RoiScenarioInput


def load_scenario_from_json(file_path: str) -> RoiScenarioInput:
    """Load and validate a scenario from a JSON file."""
    with open(file_path, "r") as file:
        data = json.load(file)
    return RoiScenarioInput(**data)