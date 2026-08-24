# GameCharacter

A simple Python class for representing a game character with `health`, `mana`, and `level` attributes. Uses Python properties to enforce safe value ranges and provides a clean leveling system.

## Features

- **Encapsulated attributes** — `name`, `health`, `mana`, and `level` are protected via properties, preventing invalid values from being set directly.
- **Automatic range clamping** — `health` and `mana` setters keep values within valid bounds (0–100 and 0–50 respectively).
- **Leveling system** — `level_up()` increases the character's level and fully restores health and mana.
- **Readable output** — a custom `__str__` method prints a formatted character summary.

## Requirements

- Python 3.6+
- No external dependencies

## Usage

```python
from game_character import GameCharacter

# Create a new character
hero = GameCharacter("Aria")

# Access read-only properties
print(hero.name)    # Aria
print(hero.level)   # 1

# Modify health and mana (values are automatically validated)
hero.health = 75
hero.mana = 30

# Level up the character
hero.level_up()

# Print character info
print(hero)
```

### Example Output

```
Aria leveled up to 2!
Name: Aria
Level: 2
Health: 100
Mana: 50
```

## Class Reference

### `GameCharacter(name)`
Creates a new character with the given name, starting at level 1 with 100 health and 50 mana.

| Property | Type | Description |
|----------|------|-------------|
| `name`   | `str` (read-only) | The character's name. |
| `health` | `int` (0–100) | Current health. Values below 0 are clamped to 0; values outside the valid range are ignored by the setter. |
| `mana`   | `int` (0–50)  | Current mana. Values below 0 are clamped to 0; values outside the valid range are ignored by the setter. |
| `level`  | `int` (read-only) | Current character level. |

### `level_up()`
Increases `level` by 1, resets `health` to 100 and `mana` to 50, and prints a level-up message.

### `__str__()`
Returns a formatted multi-line string summarizing the character's name, level, health, and mana.

## Notes on Current Behavior

- The `health` and `mana` setters only clamp values **below** 0. Values above the maximum (100 for health, 50 for mana) that don't fall within the valid range are silently ignored rather than clamped to the max — this may be worth revisiting if you want strict upper-bound clamping (e.g. `health = 500` currently leaves `health` unchanged instead of capping it at 100).

## License

Add your preferred license here (e.g. MIT).
