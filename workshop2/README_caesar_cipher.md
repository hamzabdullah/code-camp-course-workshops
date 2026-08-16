# Caesar Cipher (caesar-cipher.py)

A simple Python script implementing the classic Caesar cipher for encrypting and decrypting text, shifting each letter of the alphabet by a fixed number of positions.

## Features

- Encrypt and decrypt text using a Caesar shift cipher
- Preserves letter case (uppercase stays uppercase, lowercase stays lowercase)
- Leaves non-alphabetic characters (numbers, spaces, punctuation) unchanged
- Validates that the shift value is an integer between 1 and 25

## Requirements

- Python 3.6+
- No external dependencies

## Usage

```python
from caesar_cipher import encrypt, decrypt

encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)
# iuhhFrghFdps

decrypted_text = decrypt(encrypted_text, 3)
print(decrypted_text)
# freeCodeCamp
```

> Note: since the file is named `caesar-cipher.py` with a hyphen, it can't be imported directly with `import caesar-cipher` (hyphens aren't valid in Python identifiers). Either run the script directly, or rename it to `caesar_cipher.py` if you want to import its functions elsewhere.

## Functions

| Function | Description |
|---|---|
| `caesar(text, shift, encrypt=True)` | Core function. Shifts every letter in `text` by `shift` positions. If `encrypt=False`, shifts in the opposite direction (decryption). Returns an error message string if `shift` isn't a valid integer between 1 and 25. |
| `encrypt(text, shift)` | Convenience wrapper — encrypts `text` by shifting forward. |
| `decrypt(text, shift)` | Convenience wrapper — decrypts `text` by shifting backward. |

## How it works

- The alphabet is rotated by `shift` positions (e.g. with `shift=3`, `a → d`, `b → e`, ..., `z → c`).
- `str.maketrans` builds a translation table mapping each original letter (upper and lower) to its shifted counterpart.
- `text.translate()` applies that mapping across the whole input string in one pass.
- For decryption, the shift is simply negated, rotating the alphabet the opposite way.

## Validation rules

- `shift` must be an `int` — passing a float, string, etc. returns `'Shift must be an integer value.'`
- `shift` must be between 1 and 25 inclusive — otherwise returns `'Shift must be an integer between 1 and 25.'`
  (A shift of 0 or 26 would leave the text unchanged, and shifts are only meaningful within a 26-letter alphabet.)

## Notes / Limitations

- Only the English alphabet (a–z, A–Z) is shifted; digits, punctuation, and spaces pass through unchanged.
- On an invalid shift, the function returns a plain error string rather than raising an exception — calling code should check for this if it needs to distinguish errors from valid output.
- This is a classic (insecure) cipher intended for learning purposes, not for securing sensitive data — Caesar ciphers can be broken instantly by brute force (only 25 possible shifts) or frequency analysis.
