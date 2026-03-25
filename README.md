# Ring2Book ROI Calculator

A scenario-based ROI calculator for missed-call recovery in UK trades businesses.

This project estimates how much revenue a trades business may be losing from missed calls, how much Ring2Book could recover, and what the resulting ROI could look like under different operating assumptions.

It was built as both:

- a practical commercial modelling tool for Ring2Book
- a portfolio project to demonstrate solutions engineering, Python backend structure, API design, validation, testing, and developer workflow

## What this project does

The calculator compares two states:

- **Baseline state** — what happens today when missed calls are handled manually or lost
- **Assisted state** — what happens when Ring2Book follows up automatically and moves leads through a structured recovery funnel

It returns a summary including:

- missed calls per month
- baseline recovered revenue
- assisted recovered revenue
- incremental revenue
- monthly cost
- net monthly gain
- ROI multiple
- setup payback period

## Why this matters

Generic ROI claims are easy to say but hard to trust. This project turns that into a transparent, reusable model with:

- validated structured inputs
- reusable scenario files
- tested calculation logic
- command-line execution
- API access through FastAPI

## Architecture

This project is structured in layers:

- **Scenario inputs** — JSON files define reusable business cases such as plumbing and electrical trades
- **Validation layer** — Pydantic models validate the input shape and rules before calculations run
- **Calculation layer** — small Python functions calculate baseline revenue, assisted revenue, incremental revenue, ROI, and payback
- **CLI layer** — a command-line runner makes the calculator easy to execute locally
- **API layer** — FastAPI exposes the calculator through browser-accessible endpoints and Swagger docs
- **Test layer** — Pytest checks the calculator, scenarios, and CLI behavior

## Tech stack

- Python
- Pydantic
- Pytest
- FastAPI
- Uvicorn
- JSON scenario files

## Key outcomes

This project now supports:

- reusable scenario files for multiple trade types
- validated input handling with Pydantic
- tested ROI calculation logic
- command-line execution for local usage
- browser-accessible API endpoints through FastAPI
- interactive API docs through Swagger

## Key outcomes

This project now supports:

- reusable scenario files for multiple trade types
- validated input handling with Pydantic
- tested ROI calculation logic
- command-line execution for local usage
- browser-accessible API endpoints through FastAPI
- interactive API docs through Swagger

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
│       ├── api.py
│       ├── calculator.py
│       ├── cli.py
│       ├── models.py
│       └── presets.py
├── scenarios/
│   ├── plumber_base.json
│   └── electrician_base.json
├── tests/
│   └── test_calculator.py
└── assets/
Run from the command line

From the project root, run:

$env:PYTHONPATH="src"; python -m ring2book_roi.cli scenarios/plumber_base.json

You can also run a different scenario file, for example:

$env:PYTHONPATH="src"; python -m ring2book_roi.cli scenarios/electrician_base.json
Run the API locally

From the project root, run:

$env:PYTHONPATH="src"; python -m uvicorn ring2book_roi.api:app --reload

While the server is running, open:

http://127.0.0.1:8000/health
http://127.0.0.1:8000/scenario/plumber_base
http://127.0.0.1:8000/docs