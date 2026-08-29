# Quick Sort (Three-Way Partition, Functional Style)

A Python implementation of **quick sort** using a three-way partitioning scheme (`less`, `equal`, `greater`) and a purely functional style that returns a new sorted list instead of mutating the input.

> Lab submission — implements quick sort with first-element pivot selection and Dutch national flag–style partitioning.

## How It Works

1. **Base case**: If the list has 0 or 1 elements, it's already sorted — return a copy of it.
2. **Choose pivot**: Always pick the **first element** (`numbers[0]`) as the pivot.
3. **Partition**: Loop through every element in `numbers` and bucket it into one of three lists:
   - `less` — elements smaller than the pivot
   - `equal` — elements equal to the pivot (including the pivot itself)
   - `greater` — elements larger than the pivot
4. **Recurse and combine**: Recursively sort `less` and `greater`, then concatenate the results as `quick_sort(less) + equal + quick_sort(greater)`.

Because partitioning happens against a fixed pivot value (not swapping elements in place), this naturally produces a **stable-by-value**, three-way split — all duplicates of the pivot land together in the middle without needing extra recursive calls.

## Function Signature

```python
quick_sort(numbers)
```

### Parameters

| Parameter | Type | Description                                  |
|-----------|------|------------------------------------------------|
| `numbers` | list | The list of comparable elements to sort.       |

### Returns

- A **new** `list` containing the elements of `numbers` in sorted order. The original input list is not modified.

## Example Usage

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)
# Output: [1, 2, 4, 5, 6, 8, 10, 14]

print(numbers)
# Output: [4, 10, 6, 14, 2, 1, 8, 5]  <- unchanged, since quick_sort returns a new list
```

## Edge Cases Handled

- **Empty list (`[]`)** → base case, returns `[]`.
- **Single-element list** → base case, returns a copy of the same single-element list.
- **Duplicate values** → all values equal to the pivot go into `equal` and are placed directly in the final result without further recursion, so duplicates are handled efficiently and correctly.
- **Already sorted / reverse sorted input** → handled correctly, but see the time complexity note below on why this is a *worst case* for performance.

## Complexity Analysis

### Time Complexity

- **Best / Average case: O(n log n)**
  When the pivot roughly splits the list in half each time, there are `O(log n)` levels of recursion, and each level does `O(n)` work to partition — giving `O(n log n)` overall.

- **Worst case: O(n²)**
  Since the pivot is always `numbers[0]`, an already-sorted or reverse-sorted input causes maximally unbalanced partitions (`less` or `greater` ends up with `n - 1` elements every time). This degrades to `O(n²)`, same as a naive insertion/selection sort — a well-known weakness of fixed first-element pivoting.

### Space Complexity: O(n)

- Unlike an in-place quicksort (which typically uses `O(log n)` stack space via index swapping), this implementation builds **new lists** (`less`, `equal`, `greater`) at every recursive call and concatenates them with `+`.
- This means auxiliary space is **O(n) per level of recursion**, and since recursion depth can range from `O(log n)` (balanced case) to `O(n)` (worst case, sorted/reverse-sorted input), total space usage is:
  - **O(n log n)** in the best/average case (across all levels)
  - **O(n²)** in the worst case
  
  Either way, this is significantly more memory-hungry than a classic swap-based in-place quicksort, since new lists are allocated at every single recursive call rather than sorting within the original array.

## Notes

- **Pivot choice matters a lot here.** Since the pivot is always the first element, this implementation is vulnerable to `O(n²)` worst-case behavior on already-sorted, reverse-sorted, or adversarially crafted input. A common improvement is to pick a **random pivot** or use **median-of-three** pivot selection to make worst-case behavior far less likely in practice.
- This version is **not in-place** — it favors readability and simplicity (no index bookkeeping, no swaps) over the memory efficiency of a traditional Lomuto/Hoare partition scheme.
