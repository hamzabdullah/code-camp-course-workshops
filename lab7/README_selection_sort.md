# Selection Sort

A Python implementation of **selection sort** — a simple in-place comparison sort that repeatedly finds the minimum element from the unsorted portion of the list and swaps it into its correct sorted position.

> Lab submission — implements the classic selection sort algorithm with in-place swapping.

## How It Works

1. Loop through the list with index `i`, representing the boundary between the sorted (left) and unsorted (right) portions.
2. Assume the element at `i` is the minimum (`min_index = i`).
3. Scan the remaining unsorted elements (`j` from `i + 1` to the end) to find the actual smallest value, updating `min_index` whenever a smaller element is found.
4. After scanning, if the minimum found isn't already at position `i`, swap `items[i]` and `items[min_index]`.
5. Repeat until `i` reaches the end of the list — at which point everything is sorted.

Each pass "selects" the correct next-smallest element and places it at the front of the unsorted region, hence the name.

## Function Signature

```python
selection_sort(items)
```

### Parameters

| Parameter | Type | Description                                    |
|-----------|------|--------------------------------------------------|
| `items`   | list | The list of comparable elements to sort, mutated in place. |

### Returns

- The same `list` object passed in, now sorted in ascending order. (It both mutates `items` in place **and** returns it.)

## Example Usage

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
result = selection_sort(numbers)
print(result)
# Output: [1, 2, 4, 5, 6, 8, 10, 14]

print(numbers)
# Output: [1, 2, 4, 5, 6, 8, 10, 14]  <- same list object, sorted in place
```

## Edge Cases Handled

- **Empty list (`[]`)** → outer loop never executes, returns `[]` unchanged.
- **Single-element list** → outer loop runs once with no inner comparisons, returns the list unchanged.
- **Duplicate values** → handled correctly; `<` comparison means the first occurrence of the minimum value is chosen, which keeps relative order stable among duplicates that are already in their minimal positions, though a swap can shift others (see stability note below).
- **Already sorted input** → still runs the full `O(n²)` comparison scan even though no swaps are needed — selection sort does not have a "best case" shortcut like insertion sort or bubble sort do.

## Complexity Analysis

### Time Complexity: O(n²) — best, average, and worst case

- The outer loop runs `n` times.
- For each outer iteration `i`, the inner loop scans the remaining `n - i - 1` elements to find the minimum.
- Total comparisons: `(n-1) + (n-2) + ... + 1 + 0 = n(n-1)/2`, which is **O(n²)**.
- Unlike bubble sort or insertion sort, selection sort **always** performs the full number of comparisons regardless of input order — even a fully sorted list takes just as long to scan, since the algorithm has no way to detect "already sorted" early.
- **Swaps**, however, are minimal: at most `n - 1` swaps total (one per outer iteration, only if `min_index != i`), which makes selection sort useful in scenarios where **write operations are expensive** (e.g., flash memory) even though comparisons are plentiful.

### Space Complexity: O(1)

- Sorting happens entirely in place using the original `items` list.
- Only a fixed number of scalar variables (`i`, `j`, `min_index`) are used regardless of input size — no auxiliary arrays or recursion.

## Notes

- **Not a stable sort.** Swapping `items[i]` and `items[min_index]` can move an element past other equal elements in between, changing their relative order. For example, sorting `[(2, 'a'), (1, 'x'), (2, 'b')]` by first value alone would not necessarily preserve the original `'a'` before `'b'` ordering after the swap at index 0.
- Because comparisons are always `O(n²)` regardless of input, selection sort is generally **slower in practice** than insertion sort for small or nearly-sorted lists, despite having the same worst-case complexity. Its main advantage is the low, predictable number of swaps (`O(n)`).
