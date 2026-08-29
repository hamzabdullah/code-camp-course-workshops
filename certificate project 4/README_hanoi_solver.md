# Tower of Hanoi Solver

A Python implementation of the classic **Tower of Hanoi** puzzle solver, using recursion to compute the full sequence of moves required to transfer `n` disks from one rod to another, following the puzzle's rules.

> Certificate project — implements a recursive solution to the Tower of Hanoi problem and returns a complete move-by-move trace of the rod states.

## The Puzzle

Tower of Hanoi is a classic puzzle with three rods and `n` disks of different sizes, all starting stacked on the first rod in order of decreasing size (largest at the bottom). The goal is to move the entire stack to another rod, following three rules:

1. Only **one disk** can be moved at a time.
2. Each move takes the **top disk** from one stack and places it on top of another stack.
3. A larger disk can **never** be placed on top of a smaller disk.

## How It Works

- **State representation**: `rods` is a list of three lists, each representing a rod as a stack. `rods[0]` starts with all `n` disks (`range(n, 0, -1)`, so the largest disk is at the bottom / start of the list and the smallest is at the top / end). `rods[1]` and `rods[2]` start empty.
- **`record_move()`**: Captures a snapshot of all three rods' current contents as a single space-separated string and appends it to the `moves` list. This is called once before any moves (the starting position) and once after every disk move.
- **`move_disks(number, source, target, auxiliary)`**: The recursive core of the algorithm.
  - **Base case**: If `number == 0`, there's nothing to move — return immediately.
  - **Recursive case**: To move `number` disks from `source` to `target` using `auxiliary` as the spare rod:
    1. Recursively move the top `number - 1` disks from `source` to `auxiliary` (using `target` as the spare for that sub-problem).
    2. Move the single largest remaining disk directly from `source` to `target` (via `rods[source].pop()` and `rods[target].append(disk)`), then record this move.
    3. Recursively move the `number - 1` disks now sitting on `auxiliary` over to `target` (using `source` as the spare).
- **Entry point**: `hanoi_solver(n)` initializes the rods, records the starting state, then kicks off `move_disks(n, 0, 2, 1)` — move all `n` disks from rod `0` to rod `2`, using rod `1` as the auxiliary. Finally, it joins all recorded states into one newline-separated string and returns it.

## Function Signature

```python
hanoi_solver(n)
```

### Parameters

| Parameter | Type | Description                                   |
|-----------|------|-------------------------------------------------|
| `n`       | int  | The number of disks to solve the puzzle for. Should be a non-negative integer. |

### Returns

- A `str`: every rod state (starting position plus one line per move), separated by newlines. Each line shows the three rods' contents as `[largest...smallest] [] []`-style lists.

## Example Usage

```python
print(hanoi_solver(3))
```

Output:
```
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

Each line is a full snapshot of the three rods at that point in time — the first line is the starting position, and the last line shows all disks successfully transferred to rod 3 (index 2), in the correct order.

```python
print(hanoi_solver(0))
# Output: "[] [] []"   (just the starting/only state, no moves needed)

print(hanoi_solver(1))
# Output:
# "[1] [] []
# [] [] [1]"
```

## Edge Cases Handled

- **`n = 0`** → `move_disks(0, ...)` immediately hits the base case and returns without recursing further. Only the initial `record_move()` call contributes output, so the result is just the empty starting state.
- **`n = 1`** → resolves in a single move, no recursion needed beyond the base case check.

## Complexity Analysis

### Time Complexity: O(2ⁿ)

- Let `T(n)` be the number of calls needed to move `n` disks. The recurrence relation is:
  ```
  T(n) = 2·T(n-1) + O(1)
  T(0) = O(1)
  ```
- Solving this recurrence gives `T(n) = O(2ⁿ)`.
- This matches the well-known minimum number of moves required to solve Tower of Hanoi with `n` disks: **exactly `2ⁿ - 1` moves**. This is a mathematically proven lower bound — no algorithm can solve the classic 3-rod Tower of Hanoi in fewer moves, so the exponential time complexity is inherent to the problem itself, not a weakness of this particular implementation.
- Each move additionally calls `record_move()`, which does `O(n)` work to serialize the three rods into a string (proportional to the number of disks across all rods). This adds a multiplicative `O(n)` factor to each move, making the *true* total time complexity **O(n · 2ⁿ)** when accounting for the string-building overhead, though the move count itself is `O(2ⁿ)`.

### Space Complexity: O(n)

- **Recursion depth**: The call stack depth for `move_disks` is at most `n` (each recursive level decreases `number` by 1 until reaching the base case), so the stack contributes `O(n)` space.
- **`rods`**: Always holds exactly `n` disks total across the three lists at any point in time → `O(n)`.
- **`moves`**: This is the dominant space consumer overall — it stores a string snapshot of all three rods for *every* move, and there are `O(2ⁿ)` moves, each snapshot itself being `O(n)` in size. So the `moves` list alone occupies **O(n · 2ⁿ)** space by the time the function returns.

So while the *algorithmic* recursion itself only needs O(n) auxiliary space, the practice of **recording every intermediate state** for output means the actual memory footprint of the returned result grows as **O(n · 2ⁿ)** — this is worth calling out explicitly, since it's the more meaningful real-world constraint on how large an `n` you can practically run (e.g., `n = 20` already produces over a million moves).

## Notes

- This implementation prioritizes **full visibility into the solving process** (every intermediate rod state) over efficiency — a version that only needed the *list* of moves (e.g., "move disk from rod A to rod C") rather than a full state snapshot at each step would be far more memory-efficient, since it wouldn't need to serialize all three rods on every move.
- The exponential move count (`2ⁿ - 1`) is a defining, unavoidable characteristic of the Tower of Hanoi problem — it's often used as a canonical teaching example for recursion and for illustrating exponential time complexity in algorithms courses.
