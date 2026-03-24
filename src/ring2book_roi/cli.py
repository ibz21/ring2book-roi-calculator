import sys

from ring2book_roi import calculate_roi_summary, load_scenario_from_json


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m ring2book_roi.cli <scenario_json_path>")
        sys.exit(1)

    scenario_path = sys.argv[1]
    scenario = load_scenario_from_json(scenario_path)
    summary = calculate_roi_summary(scenario)

    print(summary)


if __name__ == "__main__":
    main()