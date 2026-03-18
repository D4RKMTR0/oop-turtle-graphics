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
├── turtle_manage.py # Turtle and TurtleManager classes.
├── shapes.py        # Circle, Square, Triangl
├── persistence.py   # save/load JSON
└── data/
    └── drawing.json
```

## Status

Work in progress. Currently working on shape drawing logic for turtles.

## Usage

```bash
python main.py
```

---

*Part of my learning journal. Code gets cleaner as I go.*
