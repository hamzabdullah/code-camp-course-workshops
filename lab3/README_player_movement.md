# Player Interface (Lab)

> **Note:** Ye lab ka naam **"Player Interface"** hai — ek academic exercise jo OOP concepts (Abstraction, Inheritance) practice karne ke liye likhi gayi hai.

Ek simple Python program jo **Abstract Base Class** use karke ek grid-based movement system banata hai, jaisa chess jaise games mein hota hai.

## Kya karta hai?

- Ek `Player` abstract class hai jisme common movement logic hoti hai.
- `Pawn` class us se inherit karti hai aur apni specific moves define karti hai.
- Player random move choose karta hai apni allowed moves list se, aur apni position + path update karta hai.
- `level_up()` call karne par Pawn ki moves list mein diagonal moves bhi add ho jate hain (jaise upgrade hone ke baad extra abilities mil jayein).

## Files

- `main.py` – Poora code (`Player` abstract class aur `Pawn` class)

## Kaise Chalayein

```bash
python main.py
```

*(Note: File mein filhal koi direct run/test code nahi hai — Pawn object banake `make_move()` aur `level_up()` call kar ke test kar sakte hain.)*

### Example Usage

```python
p = Pawn()
print(p.make_move())   # random move -> position update
p.level_up()            # diagonal moves add ho gaye
print(p.make_move())    # ab diagonal move bhi possible
print(p.path)           # abhi tak ka pura path
```

## Code Structure

| Class | Kaam |
|---|---|
| `Player` (Abstract) | Base class — moves, position, path store karti hai; `make_move()` common logic |
| `Pawn` | `Player` se inherit karti hai; apni starting moves (up/down/left/right) define karti hai |

## Concepts Used

- **Abstraction** (`ABC`, `@abstractmethod`)
- **Inheritance** (`Pawn` extends `Player`)
- **Encapsulation** of movement state (`position`, `path`, `moves`)

## Requirements

- Python 3.x

## License

Academic / Lab purpose only.
