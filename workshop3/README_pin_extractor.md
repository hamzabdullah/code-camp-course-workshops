# Pin Extractor (pin-extractor.py)

A Python script that derives a numeric "secret code" from a poem, based on the length of specific words in each line.

## How it works

For each poem:
- The poem is split into lines.
- For each line (by index, starting at 0), the line is split into words.
- If the line has *more* words than its own line index, the word at that index's length (number of characters) is appended to the code as a digit.
- Otherwise, `'0'` is appended for that line.
- The digits from every line are concatenated into one string — the poem's "secret code."

This is repeated for every poem passed in, building up a list of codes.

## Requirements

- Python 3.6+
- No external dependencies

## Usage

```python
from pin_extractor import pin_extractor

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

codes = pin_extractor([poem, poem2, poem3])
print(codes)
```

> Note: since the file is named `pin-extractor.py` with a hyphen, it can't be imported directly with `import pin-extractor` (hyphens aren't valid in Python identifiers). Either run the script directly, or rename it to `pin_extractor.py` if you want to import its functions elsewhere.

## Function

| Function | Description |
|---|---|
| `pin_extractor(poems)` | Takes an **iterable of poems** (strings) and computes a secret code for each, based on word lengths at matching line/word indices. |

### Parameters

- `poems`: a list (or other iterable) of strings, where each string is a poem with lines separated by `\n`.

## ⚠️ Known issue: missing return value

As currently written, `pin_extractor` builds up the `secret_codes` list internally but **never returns it** — the function implicitly returns `None`. To actually get the codes back, add a `return secret_codes` statement at the end of the function:

```python
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes   # <-- add this line
```

## Notes / Limitations

- `pin_extractor` expects a **list of poems**, not a single poem string — passing one poem directly (e.g. `pin_extractor(poem)`) will iterate over its lines instead of treating it as one poem, giving incorrect results.
- Word "length" only counts characters as split by whitespace, so punctuation attached to a word (commas, periods, etc.) is included in the character count.
- If a line has fewer words than its line index requires, the code digit for that line is always `'0'`, regardless of how the line is otherwise structured.
- Since digits used are just word lengths, codes aren't guaranteed to be unique across different poems.
