# Number Pattern Generator (number-pattern-generator.py)

A simple Python script that generates a space-separated sequence of numbers from 1 up to a given integer `n`.

## Features

- Generates the sequence `1 2 3 ... n` as a single string
- Validates that the input is a "real" integer (rejects booleans, since `bool` is technically a subclass of `int` in Python)
- Validates that the input is greater than 0

## Requirements

- Python 3.6+
- No external dependencies

## Usage

```python
from number_pattern_generator import number_pattern

print(number_pattern(5))
# "1 2 3 4 5"

print(number_pattern(1))
# "1"

print(number_pattern(-3))
# "Argument must be an integer greater than 0."

print(number_pattern(2.5))
# "Argument must be an integer value."

print(number_pattern(True))
# "Argument must be an integer value."
```

> Note: since the file is named `number-pattern-generator.py` with hyphens, it can't be imported directly with `import number-pattern-generator` (hyphens aren't valid in Python identifiers). Either run the script directly, or rename it to `number_pattern_generator.py` if you want to import its function elsewhere.

## Function

| Function | Description |
|---|---|
| `number_pattern(n)` | Returns a string of numbers from `1` to `n`, separated by spaces. Returns an error message string if `n` isn't a valid positive integer. |

### Parameters

- `n`: the integer up to which the sequence is generated (must be `> 0`).

## Validation rules

- `n` must be an `int` — floats, strings, `None`, etc. return `'Argument must be an integer value.'`
- `n` must **not** be a `bool` — even though `True`/`False` are technically `int` in Python, they're explicitly excluded and also return `'Argument must be an integer value.'`
- `n` must be greater than 0 — otherwise returns `'Argument must be an integer greater than 0.'`

## Notes / Limitations

- On invalid input, the function returns a plain error message string rather than raising an exception — calling code should check for this if it needs to distinguish errors from valid output.
- There's no upper limit on `n`, so very large values will produce very long strings and may be slow to generate.
- The output is a single space-separated string, not a list — if you need the numbers as integers or a list, you'd need to parse the result (e.g. `[int(x) for x in number_pattern(5).split()]`).
