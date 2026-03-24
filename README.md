# Ring2Book ROI Calculator

A scenario-based ROI calculator for missed-call recovery in UK trades businesses.

This project models the difference between:

- the current state: missed calls handled manually or lost
- the assisted state: Ring2Book follow-up workflow with automated outreach, qualification, booking, and completion

The goal is to turn prospect-specific inputs into a transparent monthly recovery estimate and ROI output.

## Why this project exists

In solutions engineering and pre-sales, generic ROI claims are weak. This tool is designed to produce a prospect-specific commercial case using clear assumptions and reusable logic.

It is also being built as a portfolio project to demonstrate:

- solutions engineering thinking
- commercial modelling
- Python backend structure
- API-ready design
- testing discipline

## Initial scope

Version 1 models:

- inbound calls
- missed-call rate
- current manual recovery
- booking conversion
- completion rate
- average job value
- Ring2Book-assisted recovery funnel
- monthly revenue recovery
- ROI multiple
- setup payback period
- multiple reusable scenario files for different trade types

## Planned build stages

1. Define calculator scope and assumptions
2. Create input schema
3. Build Python calculation engine
4. Add tests
5. Add scenario presets
6. Expose via FastAPI
7. Add simple front end

## Project structure

```text
ring2book-roi-calculator/
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   └── calculator-spec.md
├── src/
│   └── ring2book_roi/
│       ├── __init__.py
│       ├── models.py
│       ├── calculator.py
│       └── presets.py
├── scenarios/
│   └── plumber_base.json
├── tests/
│   └── test_calculator.py
└── assets/

## Run from the command line

From the project root, run:

```powershell
$env:PYTHONPATH="src"; python -m ring2book_roi.cli scenarios/plumber_base.json