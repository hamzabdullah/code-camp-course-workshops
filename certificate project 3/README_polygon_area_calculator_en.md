# Polygon Area Calculator

> **Note:** This is my **Certificate Project**, built using OOP concepts (Inheritance, Polymorphism).

A Python program that calculates the area, perimeter, and diagonal of `Rectangle` and `Square` shapes, and can also visually print them using `*` characters.

## What it does

- `Rectangle` is the base shape class that lets you set width/height and calculate area, perimeter, and diagonal.
- `Square` inherits from `Rectangle` (since a square is essentially a special rectangle where width = height).
- `get_picture()` prints the shape using `*` characters (returns "Too big for picture." if width or height exceeds 50).
- `get_amount_inside()` tells you how many times a smaller shape can fit inside a larger one.

## Files

- `main.py` – Full code (`Rectangle` and `Square` classes)

## How to Run

```bash
python main.py
```

### Example Usage

```python
rect = Rectangle(10, 5)
print(rect.get_area())        # 50
print(rect.get_perimeter())   # 30
print(rect.get_diagonal())    # 11.18
print(rect)                   # Rectangle(width=10, height=5)

sq = Square(9)
print(sq.get_area())          # 81
print(sq)                     # Square(side=9)

print(rect.get_picture())

print(rect.get_amount_inside(sq))  # how many times sq fits inside rect
```

## Code Structure

| Class / Method | Purpose |
|---|---|
| `Rectangle` | Base class — width, height, area, perimeter, diagonal, picture |
| `Square` | Inherits from `Rectangle` — setting the side updates both width & height |
| `get_area()` | Calculates the area |
| `get_perimeter()` | Calculates the perimeter |
| `get_diagonal()` | Calculates the diagonal length (Pythagoras theorem) |
| `get_picture()` | Prints the shape using `*` characters |
| `get_amount_inside()` | Tells how many times another shape fits inside |

## Concepts Used

- **Inheritance** (`Square` extends `Rectangle`)
- **Method Overriding** (`set_width`, `set_height`, `__str__`)
- **Encapsulation**

## Requirements

- Python 3.x

## License

Certificate Project — for personal learning purposes.
