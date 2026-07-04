# Release checklist

## v1.0.0

Release type: initial public portfolio release.

## Before publishing

- [ ] Repository is pushed to GitHub.
- [ ] README renders correctly.
- [ ] `screenshots/preview.png` exists.
- [ ] `dist/`, `build/`, `__pycache__/` are not committed.
- [ ] Windows build was tested from a clean extracted ZIP.
- [ ] Release asset uses this name:

```text
Interactive-Fractal-Generator-v1.0.0-windows-x64.zip
```

## Manual Windows build test

1. Copy the release ZIP to a clean folder, for example `Downloads`.
2. Extract the ZIP.
3. Open the extracted folder.
4. Run `main.exe`.
5. Confirm that:
   - the GUI starts,
   - sliders/dials update the fractal,
   - SVG export works,
   - the app closes normally.

## Suggested GitHub release text

```markdown
# Interactive Fractal Generator v1.0.0

Initial public release of the Interactive Fractal Generator.

This release contains a prebuilt Windows x64 version of the application.

## Highlights

- Interactive fractal tree rendering.
- Real-time parameter controls.
- HSV color variation.
- Antialiasing toggle.
- SVG export.

## How to run

1. Download `Interactive-Fractal-Generator-v1.0.0-windows-x64.zip`.
2. Extract the ZIP.
3. Run `main.exe`.

## Notes

This is a legacy academic project cleaned up for portfolio/public presentation.
The source code is intentionally kept close to the original implementation.
```
