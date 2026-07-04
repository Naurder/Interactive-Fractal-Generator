# Interactive Fractal Generator

**Interactive desktop application for exploring fractal structures in real time.**

This project was originally built as an academic Python/PyQt5 application and later cleaned up for a public portfolio repository. It focuses on live manipulation of recursive fractal parameters instead of generating a single static image.

![Application preview](screenshots/preview.png)

## What it does

The application provides a GUI for experimenting with fractal geometry. Parameters can be changed while working with the program, making it easier to observe how recursive structures react to small changes.

## Features

- Real-time fractal tree rendering.
- Interactive controls for:
  - branch angle,
  - recursion depth,
  - initial branch length,
  - left and right branch length ratios,
  - knot position,
  - zoom,
  - start rotation,
  - brush thickness.
- Rendering options:
  - antialiasing,
  - left/right branch distinction,
  - line, rectangle, circle and triangle drawing modes,
  - HSV-based color variation.
- SVG export for generated fractals.
- Example generated outputs included in the repository.

## Tech stack

- Python
- PyQt5
- NumPy
- SciPy
- pandas

## Project structure

```text
Interactive-Fractal-Generator/
├── main.py                  # Main GUI application
├── FractalTreeClass.py       # Fractal rendering engine
├── requirements.txt
├── README.md
├── LICENSE
├── screenshots/
│   └── preview.png
├── examples/
└── docs/
```

## Running from source

> The project was originally developed on Windows with Python 3.10.

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

## Windows build

A prebuilt Windows version can be published through GitHub Releases.

Recommended release asset name:

```text
Interactive-Fractal-Generator-v1.0.0-windows-x64.zip
```

The ZIP should contain the full PyInstaller `dist/main` directory, not only `main.exe`.

## Notes

This repository intentionally keeps the original implementation close to its initial form. The goal of this version is to preserve and present a completed project clearly, rather than rewrite it from scratch.

## License

MIT License.
