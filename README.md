# Interactive Fractal Generator

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)](https://pypi.org/project/PyQt5/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Download for Windows](https://img.shields.io/badge/Download-Windows%20x64-blue?style=for-the-badge)](../../releases/latest)

Interactive desktop application for generating and exploring fractal trees in real time.

Built with Python and PyQt5.

---

## Preview

![Interactive Fractal Generator preview](screenshots/preview.png)

---

## Demo

Real-time parameter editing:

![Interactive Fractal Generator demo](screenshots/demo.gif)

Additional generation example:

![Interactive Fractal Generator demo 2](screenshots/demo2.gif)

---

## Features

### Fractal generation

- Interactive fractal tree generation.
- Live parameter editing through a PyQt5 GUI.
- Controls for recursive depth, branch angle, branch ratios, zoom and positioning.
- Branches that would become smaller than a few visible pixels are skipped to reduce unnecessary rendering load.

### Rendering options

- Antialiasing toggle.
- Optional left/right branch distinction.
- Brush thickness control.
- Painter modes:
  - line,
  - circle,
  - rectangle,
  - triangle.
- Optional HSV-based color control.

### Positioning

The generated fractal can be positioned on a 9-point canvas grid:

| Top Left | Top Center | Top Right |
|---|---|---|
| Middle Left | Center | Middle Right |
| Bottom Left | Bottom Center | Bottom Right |

### Export

- Export generated fractals to SVG.
- The SVG canvas is intentionally large, so very large fractals can fit inside the output.
- When opening exported SVG files in a browser or vector editor, the fractal may not appear centered at first. Pan/zoom to locate it and crop or adjust the SVG manually if needed.

---

## Performance note

The generation count has the biggest impact on performance. Higher values can create a very large number of branches and may freeze the application or slow down the computer.

Start with a low generation count and increase it gradually while watching for lag. Around **10 generations** is a reasonable neutral starting point for exploration.

---

## Download

The latest packaged Windows build is available on the [Releases](../../releases/latest) page.

1. Download the latest `windows-x64.zip` archive.
2. Extract the full archive.
3. Run:

```text
main.exe
```

> Do not extract only `main.exe`. The bundled dependencies from the ZIP archive are required.

---

## Run from source

### Requirements

- Python 3.x
- PyQt5
- NumPy
- SciPy
- pandas

### Setup on Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

The project was originally developed and tested on Windows. Other operating systems are not currently documented or verified.

---

## Project structure

Simplified top-level structure:

```text
Interactive-Fractal-Generator/
├── docs/
├── examples/
├── screenshots/
├── FractalTreeClass.py
├── main.py
├── requirements.txt
├── release-notes-v1.0.0.md
├── README.md
└── LICENSE
```

Main files:

- `main.py` — application entry point and PyQt5 user interface.
- `FractalTreeClass.py` — fractal tree rendering logic and drawing behavior.
- `screenshots/` — preview images and GIF demos used in this README.
- `examples/` — exported fractal examples.
- `docs/` — archived development notes.

---

## Development notes

Early design notes are archived in [`docs/development/whiteboard.jpg`](docs/development/whiteboard.jpg).

---

## License

This project is licensed under the [MIT License](LICENSE).
