# Hospital System Record Validator (hospitalsystem.py)

A Python script for validating a list of medical patient records against a defined schema, checking field types, formats, and value constraints, and printing details about any invalid entries.

## Features

- Validates a list (or tuple) of patient record dictionaries
- Checks that each record has exactly the expected set of keys
- Validates each field's type and format:
  - `patient_id` must match the pattern `P` followed by digits (case-insensitive)
  - `age` must be an integer, 18 or older
  - `gender` must be `"male"` or `"female"` (case-insensitive)
  - `diagnosis` must be a string or `None`
  - `medications` must be a list of strings
  - `last_visit_id` must match the pattern `V` followed by digits (case-insensitive)
- Prints a clear message identifying exactly which record and field failed, and why
- Returns `True`/`False` indicating whether the entire dataset is valid

## Requirements

- Python 3.6+ (uses f-strings, `re` module from the standard library)
- No external dependencies

## Usage

```python
from hospitalsystem import validate, medical_records

validate(medical_records)
```

Running the file directly (`python hospitalsystem.py`) validates the built-in `medical_records` sample data and prints the results.

### Example output

If all records are valid:
```
Valid format.
```

If a record is malformed, for example:
```
Unexpected format 'age: 15' at position 2.
```

## Functions

| Function | Description |
|---|---|
| `find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id)` | Checks each field against its constraint and returns a list of field names that failed validation. |
| `validate(data)` | Validates a list/tuple of record dictionaries. Prints errors for any malformed records and returns `True` if all records are valid, `False` otherwise. |

## Expected record schema

Each record must be a dictionary with exactly these keys:

```python
{
    'patient_id': str,       # e.g. "P1001" (case-insensitive "P" + digits)
    'age': int,               # >= 18
    'gender': str,            # "male" or "female" (case-insensitive)
    'diagnosis': str or None,
    'medications': list[str],
    'last_visit_id': str,     # e.g. "V2301" (case-insensitive "V" + digits)
}
```

## Notes / Limitations

- `validate` only checks that a record's keys exactly match the expected key set — extra or missing keys mark the whole record invalid, even if the values would otherwise pass.
- `age` must be a strict `int` — a string like `"34"` or a float like `34.0` will fail validation, even though it "looks" valid.
- Patients under 18 are treated as invalid records, so this validator assumes an adult-only patient dataset.
- `diagnosis` allows `None`, but there's no similar allowance for `medications` (an empty list `[]` is valid, but `None` is not).
- The regex patterns (`p\d+`, `v\d+`) only check the ID *format*, not uniqueness — duplicate `patient_id` or `last_visit_id` values across records are not flagged.
