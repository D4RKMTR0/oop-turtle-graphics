# oop-turtle-graphics

Python turtle graphics built around OOP principles. Each shape manages its own drawing logic and serializes to JSON for save/load persistence.

## Stack

- Python 3
- `turtle` (stdlib)
- `json` (stdlib)

## Structure

```
oop-turtle-graphics/
├── main.py          # entry point
├── canvas.py        # manages turtle and shape list
├── shapes.py        # Circle, Square, Triangle
├── persistence.py   # save/load JSON
└── data/
    └── drawing.json
```

## Features

- Draw circles, squares, and triangles with a shared turtle pen
- Optional color and fill per shape
- Save and load drawings via JSON
- And most of python turtle graphics' features

## Status

Work in progress. Currently working on shape drawing logic for turtles.

## Usage

```bash
python main.py
```

---

*Part of my learning journal. Code gets cleaner as I go.*