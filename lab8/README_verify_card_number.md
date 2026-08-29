# Card Number Verification (Luhn Algorithm)

A Python implementation of the **Luhn algorithm** (also known as the "modulus 10" or "mod 10" algorithm) — a simple checksum formula widely used to validate identification numbers such as credit card numbers, IMEI numbers, and other ID numbers.

> Lab submission — implements the Luhn checksum for credit card number validation.

## How It Works

1. **Clean the input**: Strip out any hyphens (`-`) or spaces from the card number string, since these are common formatting characters (e.g. `"4111-1111-1111-1111"`).
2. **Convert to digits**: Turn the cleaned string into a list of individual integers.
3. **Reverse the digits**: Process the number from right to left, since the Luhn algorithm's doubling rule is defined relative to the rightmost (check) digit.
4. **Apply the doubling rule**: For every digit at an **odd index** in the reversed list (i.e., every *second* digit counting from the right), double its value.
   - If doubling produces a value greater than 9, subtract 9 from it (equivalent to summing the two digits of the doubled value, e.g. `8 * 2 = 16 → 1 + 6 = 7`, and `16 - 9 = 7`).
5. **Sum all digits**: Add up every digit (doubled-and-adjusted ones plus untouched ones) into a running `total`.
6. **Check the result**: If `total % 10 == 0`, the number passes the Luhn checksum and is considered `"VALID!"`; otherwise it's `"INVALID!"`.

## Function Signature

```python
verify_card_number(card_number)
```

### Parameters

| Parameter     | Type | Description                                                        |
|----------------|------|------------------------------------------------------------------------|
| `card_number`  | str  | The card number to validate, digits only or with `-`/space separators (e.g. `"4111 1111 1111 1111"`). |

### Returns

- `"VALID!"` (str) if the number satisfies the Luhn checksum.
- `"INVALID!"` (str) otherwise.

## Example Usage

```python
verify_card_number("4111111111111111")
# Output: "VALID!"   (well-known test Visa number)

verify_card_number("4111-1111-1111-1111")
# Output: "VALID!"   (dashes are stripped before processing)

verify_card_number("1234 5678 9012 3456")
# Output: "INVALID!" (fails the checksum)
```

## Edge Cases Handled

- **Formatted input** (dashes or spaces) → stripped before processing, so `"4111 1111 1111 1111"` and `"4111111111111111"` behave identically.
- **Doubled digit overflow (> 9)** → correctly reduced by subtracting 9, which is mathematically equivalent to summing the doubled digit's own digits.

## Edge Cases *Not* Handled (worth noting for the lab)

- **Non-numeric characters**: If `card_number` contains letters or other symbols after stripping dashes/spaces, `int(digit)` will raise a `ValueError`. There's no `try/except` or input validation guarding against malformed input.
- **Empty string**: `""` produces an empty `digits` list, so `total` stays `0`, and `0 % 10 == 0` → the function would return `"VALID!"` for an empty input, which is likely not the intended behavior.
- **Whitespace variants**: only literal spaces (`" "`) are stripped — tabs or other whitespace characters would cause a `ValueError`.

## Complexity Analysis

### Time Complexity: O(n)

Where `n` is the number of digits in `card_number`. The algorithm makes a small constant number of full passes over the digits:
- One pass to strip formatting characters (`.replace()`, called twice) — O(n) each.
- One pass to build the `digits` list via the list comprehension — O(n).
- One pass to reverse the list (`[::-1]`) — O(n).
- One pass through `reverse_digits` in the `for` loop to compute the total — O(n).

Since each of these passes is linear and there's a fixed number of them, the overall time complexity simplifies to **O(n)**.

### Space Complexity: O(n)

- `digits` stores a full copy of the input as integers — O(n).
- `reverse_digits` (`digits[::-1]`) creates **another** full copy of the list, reversed — O(n).
- No recursion or nested data structures are used beyond these two lists.

So overall space usage is **O(n)**, dominated by the two parallel digit lists held in memory at once (`digits` and `reverse_digits`).

## Notes

- The Luhn algorithm is a **checksum**, not a security or authenticity check — it only verifies that a number is *structurally plausible* (e.g., catches typos or simple transcription errors). It says nothing about whether the card is real, active, or belongs to anyone.
- A minor efficiency note: `reverse_digits = digits[::-1]` creates a second full-size list purely to iterate in reverse. This could be avoided by iterating over `reversed(digits)` directly (a view, not a copy), which would reduce the auxiliary space to O(1) beyond the original `digits` list.
