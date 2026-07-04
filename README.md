# Interactive Fractal Generator

Interactive desktop application for generating and exploring fractal trees in real time.

Built with **Python** and **PyQt5**.

![Application preview](screenshots/preview.png)

## Features

- Real-time fractal tree rendering.
- Live parameter controls for:
  - branch angle,
  - iteration depth,
  - initial branch length,
  - branch length ratios,
  - knot position,
  - zoom,
  - starting rotation angle,
  - brush thickness.
- Rendering options:
  - antialiasing,
  - left/right branch distinction,
  - line, rectangle, circle and triangle drawing modes,
  - HSV-based color changes.
- SVG export.

## Project structure

```text
Interactive-Fractal-Generator/
├── main.py
├── FractalTreeClass.py
├── requirements.txt
├── README.md
├── LICENSE
├── screenshots/
│   └── preview.png
├── examples/
└── docs/
```

## Requirements

- Python 3.10+
- PyQt5
- NumPy
- SciPy
- pandas

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

```bash
python main.py
```

## Notes

This project was originally created as an academic fractal generator project and later cleaned up for portfolio/public GitHub presentation.

The code is intentionally kept close to the original implementation instead of being rewritten from scratch.
