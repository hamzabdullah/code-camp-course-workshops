# Musical Instruments Inventory (musical_instruments_inventory.py)

A simple Python module that defines a `MusicalInstrument` class for representing musical instruments and printing fun facts about them.

## Features

- Create `MusicalInstrument` objects with a name and instrument type/family
- `play()` method that prints a friendly message about the instrument
- `get_fact()` method that returns a fact string about which family the instrument belongs to

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies

## Usage

```python
from musical_instruments_inventory import MusicalInstrument

oboe = MusicalInstrument('Oboe', 'woodwind')
trumpet = MusicalInstrument('Trumpet', 'brass')

oboe.play()
# The Oboe is fun to play!

print(oboe.get_fact())
# The Oboe is part of the woodwind family of instruments.

trumpet.play()
# The Trumpet is fun to play!

print(trumpet.get_fact())
# The Trumpet is part of the brass family of instruments.
```

Running the file directly (`python musical_instruments_inventory.py`) creates an Oboe and a Trumpet instance and prints their play message and fact.

## `MusicalInstrument` class

| Member | Description |
|---|---|
| `__init__(name, instrument_type)` | Creates an instrument with a `name` (e.g. `"Oboe"`) and `instrument_type` (e.g. `"woodwind"`). |
| `play()` | Prints `"The <name> is fun to play!"`. |
| `get_fact()` | Returns a string: `"The <name> is part of the <instrument_type> family of instruments."`. |

## Attributes

- `name` — the instrument's name (e.g. `"Oboe"`, `"Trumpet"`)
- `instrument_type` — the family/category the instrument belongs to (e.g. `"woodwind"`, `"brass"`, `"string"`, `"percussion"`)

## Notes / Limitations

- There's no input validation — `name` and `instrument_type` can technically be any value (including empty strings, numbers, etc.), since no type or emptiness checks are performed.
- `play()` prints directly rather than returning a string, so it can't easily be captured or reused elsewhere — only `get_fact()` returns a value.
- There's no inventory/collection built into the class itself (despite the "inventory" filename) — instruments are just created as standalone objects; you'd need to manage a list or dictionary of instances yourself to track a full inventory.
