# Discount Engine

Ek simple Python project jo **Strategy Design Pattern** use karke products par best discount calculate karta hai.

## Kya karta hai?

Ye program ek product par different discount strategies apply karta hai aur sabse **best (lowest) price** nikal deta hai.

## Features / Discount Strategies

- **Percentage Discount** – Product price par % discount (agar 70% se kam ho)
- **Fixed Amount Discount** – Fixed amount minus karta hai (agar price ka 90% us amount se zyada ho)
- **Premium User Discount** – Premium tier users ko 20% flat discount

## Files

- `main.py` – Poora code (Product, DiscountStrategy, aur DiscountEngine classes)

## Kaise Chalayein

```bash
python main.py
```

### Output Example

```
Best price for Wireless Mouse for Premium user: $40.00
```

## Code Structure

| Class | Kaam |
|---|---|
| `Product` | Product ka naam aur price store karta hai |
| `DiscountStrategy` | Abstract base class — har discount type isse inherit karta hai |
| `PercentageDiscount` | % based discount logic |
| `FixedAmountDiscount` | Fixed amount discount logic |
| `PremiumUserDiscount` | Premium users ke liye special discount |
| `DiscountEngine` | Saari applicable strategies check karke best price return karta hai |

## Requirements

- Python 3.9+ (kyunki type hints jaise `list[DiscountStrategy]` use hue hain)

## Contributing

Naya discount strategy add karna ho to bas `DiscountStrategy` class ko inherit karo aur `is_applicable()` + `apply_discount()` methods likh do.

## License

Free to use — apni marzi se modify karo.
