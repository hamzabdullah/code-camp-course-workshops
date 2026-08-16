# Budget App

A simple Python module for tracking budget categories (like Food, Clothing, Entertainment, etc.), recording deposits and withdrawals, transferring funds between categories, and visualizing spending with an ASCII bar chart.

## Features

- Create multiple budget `Category` objects (e.g., Food, Rent, Savings)
- Deposit and withdraw funds with optional descriptions
- Automatically prevent withdrawals/transfers that exceed the available balance
- Transfer funds between categories (tracked as a paired withdrawal/deposit)
- Print a formatted ledger for any category
- Generate a text-based bar chart showing percentage of total spending by category

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies

## Usage

```python
from budget_app import Category, create_spend_chart

# Create categories
food = Category("Food")
entertainment = Category("Entertainment")

# Deposit funds
food.deposit(1000, "initial deposit")
entertainment.deposit(500, "initial deposit")

# Withdraw funds
food.withdraw(105.55, "groceries")
entertainment.withdraw(45.00, "movie tickets")

# Transfer funds between categories
food.transfer(50, entertainment)

# Print a category's ledger
print(food)

# Print the spending chart across categories
print(create_spend_chart([food, entertainment]))
```

## `Category` class

| Method | Description |
|---|---|
| `__init__(name)` | Creates a category with the given name and an empty ledger. |
| `deposit(amount, description="")` | Adds a positive entry to the ledger. |
| `withdraw(amount, description="")` | Adds a negative entry if sufficient funds exist. Returns `True` on success, `False` otherwise. |
| `get_balance()` | Returns the current balance (sum of all ledger entries). |
| `transfer(amount, category)` | Withdraws from this category and deposits into another, if funds allow. Returns `True`/`False`. |
| `check_funds(amount)` | Returns `True` if `amount` is available to withdraw or transfer. |
| `__str__()` | Returns a formatted ledger display, e.g.: |

```
*************Food*************
initial deposit        1000.00
groceries               -105.55
Transfer to Entertainment -50.00
Total: 844.45
```

## `create_spend_chart(categories)`

Generates a bar chart (as a string) showing the percentage of total spending that came from each category, rounded down to the nearest 10%. Only **withdrawals** count as "spending" (deposits and incoming transfers are excluded).

Example output:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|          
 40|          
 30|          
 20|          
 10|          
  0| o  o  o  
    ----------
     F  E  S  
     o  n  a  
     o  t  v  
     d  e  i  
        r  n  
        t  g  
        a     
        i     
        n     
        m     
        e     
        n     
        t     
```

## Notes / Limitations

- `check_funds` and `withdraw`/`transfer` reject amounts greater than the current balance — negative or invalid amounts are not explicitly validated.
- `create_spend_chart` divides by `total_spending`, so it will raise a `ZeroDivisionError` if no category has any withdrawals yet.
- Percentages are floored to the nearest 10, matching how the bar chart draws in increments of 10.
