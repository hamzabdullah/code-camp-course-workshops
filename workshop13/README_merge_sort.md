# Merge Sort (In-Place Array Mutation)

A Python implementation of the classic **merge sort** algorithm — a divide-and-conquer sorting technique that recursively splits an array in half, sorts each half, and merges them back together in order.

> Lab submission — implements merge sort with in-place mutation of the original array (no return value).

## How It Works

1. **Divide**: If the array has more than one element, split it into `left_part` and `right_part` at the midpoint.
2. **Conquer**: Recursively call `merge_sort` on `left_part` and `right_part` until each sub-array has 0 or 1 elements (already sorted by definition).
3. **Merge**: Walk through `left_part` and `right_part` simultaneously, comparing elements and writing the smaller one back into `array` at `sorted_index`. Once one side is exhausted, copy over any remaining elements from the other side.

Note that this implementation does **not return** a new array — it mutates the original `array` argument in place, since `left_part` and `right_part` are sorted independently and then written back into the same `array` object that was passed in.

## Function Signature

```python
merge_sort(array)
```

### Parameters

| Parameter | Type | Description                          |
|-----------|------|---------------------------------------|
| `array`   | list | The list of comparable elements to sort, mutated in place. |

### Returns

- `None`. The input `array` is sorted **in place**.

## Example Usage

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
merge_sort(numbers)
print(numbers)
# Output: [1, 2, 4, 5, 6, 8, 10, 14]
```

Running the script directly:

```
Unsorted array: 
[4, 10, 6, 14, 2, 1, 8, 5]
Sorted array: 
[1, 2, 4, 5, 6, 8, 10, 14]
```

## Edge Cases Handled

- **Empty array (`[]`)** → `len(array) <= 1`, returns immediately, nothing to sort.
- **Single-element array** → same base case, already "sorted."
- **Duplicate values** → handled correctly since the merge step uses `<` (elements equal in value fall into the `else` branch and are still merged in stable relative order from the right side comparison).

## Complexity Analysis

### Time Complexity: O(n log n)

- The array is split in half at each recursive level → **O(log n)** levels of recursion.
- At each level, merging all the sub-arrays back together takes **O(n)** total work (every element is compared/copied once per level).
- Combined: **O(n log n)** in the best, average, and worst case — merge sort's time complexity doesn't degrade for already-sorted or reverse-sorted input, unlike quicksort.

### Space Complexity: O(n)

- Although the final result is written back into the original `array` (in place from the caller's perspective), each recursive call creates new sub-lists via slicing (`array[:middle_point]` and `array[middle_point:]`).
- These slices are auxiliary arrays that exist temporarily on the call stack. At any given time, the total extra memory used across all active slices sums to **O(n)**.
- Additionally, the recursion depth is **O(log n)**, contributing to the call stack size, but this is dominated by the O(n) auxiliary array space.

So overall: **O(n) space**, not O(1) — this is a classic trade-off point vs. in-place sorts like heapsort (O(1) space) or quicksort (O(log n) space on average).

## Notes

- This is **not a stable sort** in the strictest sense as written — when `left_part[i] == right_part[j]`, the condition `left_part[...] < right_part[...]` is `False`, so the right element is taken first. This means equal elements from the right sub-array can be placed before equal elements from the left sub-array, breaking stability. Changing `<` to `<=` would restore standard merge sort stability.
- Since slicing creates copies, this implementation is less memory-efficient than an index-based merge sort that operates on a single auxiliary buffer, but it's simpler to read and reason about.
