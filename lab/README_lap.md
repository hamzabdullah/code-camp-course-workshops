# Planet Class (lap.py)

A simple Python module that defines a `Planet` class for representing planets, with type validation on the constructor and a couple of convenience methods.

## Features

- Create `Planet` objects with a name, planet type, and host star
- Input validation: raises errors if fields aren't non-empty strings
- `orbit()` method describing the planet's motion around its star
- Readable `__str__()` representation for easy printing

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies

## Usage

```python
from lap import Planet

earth = Planet("Earth", "terrestrial", "Sun")
jupiter = Planet("Jupiter", "gas giant", "Sun")

print(earth)
# Planet: Earth | Type: terrestrial | Star: Sun

print(earth.orbit())
# Earth is orbiting around Sun...
```

Running the file directly (`python lap.py`) will create three example planets (Earth, Jupiter, Neptune) and print each one.

## `Planet` class

| Member | Description |
|---|---|
| `__init__(name, planet_type, star)` | Creates a planet. Raises `TypeError` if any argument isn't a string, and `ValueError` if any argument is an empty string. |
| `orbit()` | Returns a string describing the planet orbiting its star. |
| `__str__()` | Returns a formatted summary: `Planet: <name> | Type: <planet_type> | Star: <star>`. |

## Attributes

- `name` — the planet's name (e.g. `"Earth"`)
- `planet_type` — the kind of planet (e.g. `"terrestrial"`, `"gas giant"`, `"ice giant"`)
- `star` — the name of the star the planet orbits (e.g. `"Sun"`)

## Validation rules

- All three constructor arguments must be strings, or a `TypeError` is raised.
- None of the three arguments may be an empty string, or a `ValueError` is raised.

```python
Planet(123, "terrestrial", "Sun")     # TypeError
Planet("Earth", "", "Sun")            # ValueError
```

## Notes / Limitations

- Validation checks for empty strings (`""`) only — strings containing just whitespace (e.g. `"   "`) are still accepted.
- There's no validation on what counts as a valid `planet_type` or `star` (any non-empty string works).
- Planets are independent objects; there is no built-in registry or solar-system container to group planets sharing a star.
