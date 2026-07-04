# Interactive Fractal Generator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GUI](https://img.shields.io/badge/GUI-PyQt5-green)
![Platform](https://img.shields.io/badge/Release-Windows%20x64-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Interactive desktop application for generating, editing and exporting recursive fractals in real time.**

The project focuses on live manipulation of fractal parameters instead of generating a single static image. It was originally built as an academic Python/PyQt5 application and later cleaned up for a portfolio-ready GitHub repository.

![Application preview](screenshots/preview.png)

## Features

### Interactive fractal editing

- Real-time fractal tree generation.
- Live control over recursive parameters:
  - branch angle,
  - recursion depth,
  - initial branch length,
  - left and right branch length ratio,
  - knot position ratio,
  - zoom,
  - starting rotation angle.
- 9-point positioning system:
  - top left,
  - top center,
  - top right,
  - middle left,
  - center,
  - middle right,
  - bottom left,
  - bottom center,
  - bottom right.

### Rendering options

- Antialiasing toggle.
- Optional left/right branch distinction.
- Configurable brush thickness.
- Multiple drawing shapes:
  - line,
  - circle,
  - rectangle,
  - triangle.
- HSV-based color control with an additional color slider.

### Export

- SVG export for generated fractals.
- Vector output can be scaled to very large formats without losing quality.
- Example generated outputs are included in the repository.

## Tech stack

- Python
- PyQt5
- NumPy
- SciPy
- pandas

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

## Running from source

> The project was originally developed and tested on Windows.

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Windows release

A prebuilt Windows version is available in GitHub Releases.

Recommended asset name:

```text
Interactive-Fractal-Generator-v1.0.0-windows-x64.zip
```

The release ZIP should contain the full PyInstaller output directory, not only the `.exe` file, because the application needs its bundled libraries and runtime files.

## Notes

This repository intentionally keeps the original implementation close to its initial form. The goal of this version is to preserve and present a completed project clearly, rather than rewrite it from scratch.

The `Help/About` menu is currently a placeholder.

## License

MIT License.
