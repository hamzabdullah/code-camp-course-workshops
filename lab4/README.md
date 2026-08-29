# Build a Hash Table — Lab

This is my lab project where I built a **Hash Table** data structure from scratch in Python.

## About This Lab

A hash table stores key-value pairs by first "hashing" the key into a number, then using that number to decide where the value gets stored. For this lab, the hashing function is simple: it sums up the Unicode (ASCII) values of every character in the key string.

The goal of the lab was to implement a `HashTable` class with four methods (`hash`, `add`, `remove`, `lookup`) and pass all the provided test cases.

## How It Works

### `HashTable` class
- Has a `collection` attribute, initialized as an empty dictionary when a new `HashTable` is created.
- The `collection` dictionary stores values grouped by their hashed key. Since two different keys can produce the same hash (a "collision"), each hash bucket is itself a nested dictionary that maps the original key string to its value. This way, colliding keys don't overwrite each other.

### `hash(key)`
- Takes a string as input.
- Returns the sum of the Unicode values of each character (using Python's `ord()`).
- Example: `hash('golf')` returns `424`.

### `add(key, value)`
- Computes the hash of `key`.
- Stores `{key: value}` inside `collection` under the hashed key.
- If another key already hashes to the same value, both key-value pairs live together in the same nested dictionary (collision handling).

### `remove(key)`
- Computes the hash of `key`.
- If the key exists in the collection, deletes only that specific key-value pair (not the whole bucket, so sibling keys with the same hash are unaffected).
- If the key doesn't exist, does nothing — no error is raised.

### `lookup(key)`
- Computes the hash of `key`.
- Returns the value associated with that exact key if it exists.
- Returns `None` if the key is not found.

## The Code

```python
class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None
```

## Tests I Ran

All 22 tests for this lab passed. Here's what each one checks:

1. A `HashTable` class is defined.
2. A new `HashTable` instance starts with `collection` as an empty dictionary.
3. The class has a `hash` method.
4. `hash` takes a string as a parameter.
5. `hash` correctly returns the sum of Unicode values of a string's characters.
6. The class has an `add` method.
7. `add` takes a key and a value as parameters.
8. The class has a `remove` method.
9. `remove` takes a key as a parameter.
10. Removing a key that doesn't exist doesn't raise an error or delete anything.
11. If multiple keys hash to the same bucket, `remove` deletes only the specific key-value pair, not the whole bucket.
12. The class has a `lookup` method.
13. `lookup` takes a key as a parameter.
14. `HashTable().hash('golf')` returns `424`.
15. `HashTable().add('golf', 'sport')` stores the pair in `collection` under hash `424`.
16. `add('dear', 'friend')` and `add('read', 'book')` both land in the same nested dictionary under hash `412` (a collision).
17. When a key exists, `remove()` deletes that key and its value from `collection`.
18. `lookup('golf')` returns `'sport'` when that pair exists.
19. `lookup('golf')` returns `None` when that pair doesn't exist.
20. `lookup('cfc')` returns `None` when only `'fcc'` exists in the collection (even though they'd hash the same, the exact key must match).
21. Adding `('rose', 'flower')` results in `collection` looking like `{441: {'rose': 'flower'}}`.
22. Adding a colliding pair like `'fcc'` and `'cfc'` results in `collection` looking like `{300: {'fcc': 'coding', 'cfc': 'chemical'}}`.

## Key Takeaway

The trickiest part of this lab was handling **hash collisions** — making sure that two different keys mapping to the same hash number don't overwrite each other, and that `remove`/`lookup` operate on the exact key string, not just the hash bucket.

## Time Complexity

Let **k** = length of the key string, and **n** = number of key-value pairs already stored in the table.

| Method | Time Complexity | Notes |
|---|---|---|
| `hash(key)` | O(k) | Loops through each character once to sum `ord()` values. |
| `add(key, value)` | O(k) | O(k) to compute the hash, plus O(1) average for the dictionary insert. |
| `remove(key)` | O(k) | O(k) to compute the hash, plus O(1) average for the dictionary delete. |
| `lookup(key)` | O(k) | O(k) to compute the hash, plus O(1) average for the dictionary access. |

**Space Complexity:** O(n) — every stored key-value pair occupies one slot across the nested dictionaries.

**Why not O(n)?** None of the methods depend on how many items are already in the table. They only depend on the length of the key being processed, because Python dictionaries jump straight to the right bucket (O(1) average) instead of scanning through every existing entry. This is the core advantage of a hash table over something like a list — lookups don't get slower as the table grows.

**Caveat:** the hash function (sum of Unicode values) is collision-prone — for example, any two anagrams (like `'dear'` and `'read'`) will always hash to the same bucket. If many keys collide into one bucket, that inner dictionary grows larger, but since it's still a Python dict (not a list), lookups inside it stay O(1) average rather than degrading further.
