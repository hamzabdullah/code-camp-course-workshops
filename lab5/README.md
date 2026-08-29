# Square Root via Bisection Method

A simple Python implementation of the **bisection method** to approximate the square root of a non-negative number, without using `math.sqrt()` or the `**` power operator.

> Lab submission — implements numerical square root approximation using binary search on real numbers.

## How It Works

The bisection method works by repeatedly narrowing down a search interval `[low, high]` that is guaranteed to contain the square root:

1. Start with `low = 0` and `high = max(1, square_target)`.
2. Compute the midpoint `root = (low + high) / 2`.
3. If `root * root < square_target`, the true root lies in the upper half, so set `low = root`.
4. Otherwise, the true root lies in the lower half, so set `high = root`.
5. Repeat until the interval `(high - low)` shrinks below `tolerance`, or `max_iterations` is reached.

This is essentially binary search applied to a continuous range instead of a discrete array.

## Function Signature

```python
square_root_bisection(square_target, tolerance=1e-7, max_iterations=100)
```

### Parameters

| Parameter        | Type  | Description                                                        |
|-------------------|-------|----------------------------------------------------------------------|
| `square_target`   | float | The number to find the square root of. Must be ≥ 0.                 |
| `tolerance`       | float | Acceptable margin of error for convergence (default: `1e-7`).       |
| `max_iterations`  | int   | Maximum number of bisection steps before giving up (default: `100`).|

### Returns

- The approximate square root (`float`) if convergence is achieved.
- `None` if the method fails to converge within `max_iterations`.

### Raises

- `ValueError` if `square_target` is negative.

## Example Usage

```python
square_root_bisection(25)
# Output: The square root of 25 is approximately 4.999999998835847

square_root_bisection(0)
# Output: The square root of 0 is 0

square_root_bisection(2, tolerance=1e-10)
# Output: The square root of 2 is approximately 1.4142135623842478
```

## Edge Cases Handled

- **Negative input** → raises `ValueError`.
- **0 or 1** → returned immediately (both are their own square roots).
- **Numbers between 0 and 1** → `high` is set to `max(1, square_target)`, ensuring the interval always brackets the true root.

## Complexity Analysis

### Time Complexity: O(log(1 / tolerance))

Each iteration halves the search interval `(high - low)`. Starting from an initial interval width of roughly `high - low = max(1, square_target)`, the number of iterations needed to shrink it below `tolerance` is:

```
n ≈ log2((high - low) / tolerance)
```

So the loop runs a number of times **proportional to the number of bits of precision requested**, independent of how large `square_target` is. This is bounded above by `max_iterations`, so the worst-case time complexity is:

```
O(min(max_iterations, log2(range / tolerance)))
```

which simplifies to **O(log(1/tolerance))** for reasonable inputs — very fast, since each halving is a constant-time arithmetic operation.

### Space Complexity: O(1)

The algorithm only tracks a fixed number of scalar variables (`low`, `high`, `root`) regardless of input size or iteration count. No recursion, arrays, or auxiliary data structures are used, so memory usage does not grow with input.

## Notes

- Convergence is based on interval width (`high - low <= tolerance`), not on the difference between `root * root` and `square_target`, which is a common and valid variant of the bisection stopping criterion.
- Because it's a numerical approximation, results will differ slightly from `math.sqrt()` beyond the specified tolerance.
