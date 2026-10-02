# Delta-V-Calculator
A simple PyQt5-based Delta V calculator using the Tsiolkovsky rocket equation. It supports calculations using exhaust velocity or specific impulse and uses Python’s Decimal module for high-precision results. Built as a learning project for Python, PyQt5, and rocket science.et delta-v using the Tsiolkovsky rocket equation.

## Features

- Exhaust velocity method
- Specific impulse method
- High-precision calculations using `Decimal`
- Simple PyQt5 GUI

## Formula

`Δv = Ve × ln(m₀ / mf)`

Where:
- `Ve` = exhaust velocity
- `m₀` = initial mass
- `mf` = final mass

## Run

```bash
pip install PyQt5
python main.py
