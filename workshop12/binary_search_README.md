# Binary Search with Path Tracking

This code implements **binary search**, but with a twist: instead of just returning the index of the found value (or `-1`), it also tracks and returns the **path of values checked** along the way to reach the target.

## The Code

```python
def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle:
            return path_to_target, f"Value found at index {mid}"
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1
    
    return [], "Value not found"
```

## How It Works

1. **`path_to_target = []`** — An empty list to keep a record of every value the algorithm looks at while searching (its "path" to the target).
2. **`low` and `high`** — These define the current search range within `search_list`. `low` starts at `0`, `high` starts at the last index.
3. **`while low <= high:`** — The main search loop. It keeps going as long as there's still a valid range left to search.
4. **`mid = (low + high) // 2`** — Calculates the middle index of the current range.
5. **`value_at_middle = search_list[mid]`** — Grabs the value sitting at the middle index.
6. **`path_to_target.append(value_at_middle)`** — Every value checked (not just the final one) gets added to `path_to_target`, so we can see the full trail the algorithm took.
7. **Three possible outcomes at each step:**
   - If `value == value_at_middle` → the target is found. Return the path taken and a message with the index.
   - If `value > value_at_middle` → the target must be in the right half, so `low` moves to `mid + 1`.
   - Otherwise → the target must be in the left half, so `high` moves to `mid - 1`.
8. If the loop ends without finding the value (`low` becomes greater than `high`), the function returns an **empty list** and the message `"Value not found"`.

## Difference From Standard Binary Search

A typical binary search only returns the index (or `-1`). This version instead returns a **tuple**: `(path_to_target, message)`.

- `path_to_target` — shows every value the algorithm inspected before finding (or failing to find) the target. This is useful for visualizing or teaching how binary search "narrows down" its range step by step.
- `message` — a human-readable string saying whether the value was found (and at what index) or not found at all.
- Note: on a failed search, `path_to_target` is discarded and an empty list `[]` is returned instead — so the trail of checked values isn't preserved in the "not found" case.

## Test Cases and Traced Output

```python
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))
```

**Output:**
```
([3], 'Value found at index 2')
([3, 5, 4], 'Value found at index 3')
([], 'Value not found')
```

### Trace 1: `binary_search([1, 2, 3, 4, 5], 3)`
| Step | low | high | mid | value_at_middle | Comparison |
|---|---|---|---|---|---|
| 1 | 0 | 4 | 2 | 3 | `3 == 3` → found at index 2 |

Result: `([3], 'Value found at index 2')` — the target was found on the very first check, since it happened to be the middle element.

### Trace 2: `binary_search([1, 2, 3, 4, 5, 9], 4)`
| Step | low | high | mid | value_at_middle | Comparison |
|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 3 | `4 > 3` → search right half |
| 2 | 3 | 5 | 4 | 5 | `4 < 5` → search left half |
| 3 | 3 | 3 | 3 | 4 | `4 == 4` → found at index 3 |

Result: `([3, 5, 4], 'Value found at index 3')` — the path shows every value checked along the way (`3`, then `5`, then `4`) before landing on the target.

### Trace 3: `binary_search([1, 3, 5, 9, 14, 22], 10)`
| Step | low | high | mid | value_at_middle | Comparison |
|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 5 | `10 > 5` → search right half |
| 2 | 3 | 5 | 4 | 14 | `10 < 14` → search left half |
| 3 | 3 | 3 | 3 | 9 | `10 > 9` → search right half, `low` becomes 4 |
| — | 4 | 3 | — | — | `low > high`, loop ends |

Result: `([], 'Value not found')` — even though the path internally checked `5`, `14`, and `9`, the target `10` doesn't exist in the list, so the function returns an empty list and the "not found" message.

## Time and Space Complexity

### Time Complexity: O(log n)
Just like standard binary search, the search range is cut in half on every iteration. So the number of comparisons needed grows **logarithmically** with the size of the list, not linearly.

- For a list of `n = 6` items (like Trace 2 and 3 above), at most `log₂(6) ≈ 2.58`, so about 3 comparisons in the worst case — which matches what we saw in Trace 3 (3 steps before giving up).
- For a list of `n = 1,000,000` items, it would only take about `log₂(1,000,000) ≈ 20` comparisons — this is what makes binary search so much faster than linear search (`O(n)`) on large sorted lists.

### Space Complexity: O(log n)
This is where this version **differs from standard binary search**.

- A typical binary search only tracks `low`, `high`, and `mid` — constant extra variables, so it's **O(1)** space.
- This version also builds up `path_to_target`, appending one value every time the loop runs. Since the loop can run at most O(log n) times (the range keeps halving until it's exhausted), the `path_to_target` list can grow to at most O(log n) elements.
- **Memory usage in practice:** In Trace 1, the path holds 1 value (`[3]`). In Trace 2, it holds 3 values (`[3, 5, 4]`). In Trace 3, the internal path reaches 3 values (`[5, 14, 9]`) before the loop ends — though since the value isn't found, that path is discarded and an empty list `[]` is returned instead, so no extra memory is retained afterward.
- So while it's still very memory-efficient compared to something like storing the entire list again, it uses slightly more memory than the O(1) space of a bare-bones binary search, because of the extra bookkeeping list.

## Requirement

Just like standard binary search, this function only works correctly if `search_list` is **sorted in ascending order**. If the list isn't sorted, the `low`/`high` narrowing logic will give incorrect results.
