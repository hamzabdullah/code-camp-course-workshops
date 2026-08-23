# Employee Management Class

A simple Python class that models an `Employee` with a name, a job level, and a salary. It uses **properties** to validate data and enforce business rules — like preventing invalid levels, blocking demotions, and making sure salaries never fall below the minimum for a given level.

## Features

- **Validated attributes** — `name`, `level`, and `salary` are all backed by property setters that validate input types and values.
- **Predefined salary tiers** — each level (`trainee`, `junior`, `mid-level`, `senior`) maps to a base salary.
- **Promotion logic** — changing an employee's `level` automatically:
  - Rejects invalid or unknown levels.
  - Rejects "promoting" to the same level.
  - Rejects downgrades to a lower level.
  - Updates the salary to match the new level's base pay.
- **Salary floor** — salary can never be set below the minimum salary for the employee's current level.
- **Readable output** — `__str__` gives a human-friendly summary; `__repr__` gives an unambiguous, reconstructable representation.

## Salary Tiers

| Level       | Base Salary |
|-------------|-------------|
| trainee     | $1,000      |
| junior      | $2,000      |
| mid-level   | $3,000      |
| senior      | $4,000      |

## Usage

```python
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
# Charlie Brown: trainee

print(f'Base salary: ${charlie_brown.salary}')
# Base salary: $1000

charlie_brown.level = 'junior'
# 'Charlie Brown' promoted to 'junior'.
# Salary updated to $2000.
```

## Class Reference

### `Employee(name, level)`
Creates a new employee with the given name and starting level. Salary is automatically set to the base salary for that level.

### Properties

| Property | Description |
|----------|-------------|
| `name`   | Must be a string. Raises `TypeError` otherwise. |
| `level`  | Must be a valid key in the salary tiers. Raises `ValueError` for unknown, duplicate, or lower levels. |
| `salary` | Must be a number (`int` or `float`). Raises `ValueError` if set below the current level's base salary. |

### Exceptions Raised

- `TypeError` — when `name`, `level`, or `salary` is given the wrong data type.
- `ValueError` — when `level` is invalid, unchanged, a demotion, or when `salary` is below the minimum for the current level.

## Requirements

- Python 3.6+

## License

Feel free to use and modify this code for personal or educational projects.
