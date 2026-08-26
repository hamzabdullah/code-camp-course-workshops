# 🎬 Media Catalogue System (Python OOP Project)

Ye ek simple Python project hai jo **Object-Oriented Programming (OOP)** ka use karke ek "Media Catalogue" banata hai — jahan aap Movies aur TV Series ko ek jagah store aur manage kar sakte hain.

---

## 📌 Project Overview

Is project mein 4 main classes hain:

| Class | Kaam |
|---|---|
| `MediaError` | Custom exception — jab galat cheez catalogue mein add ki jaye |
| `Movie` | Ek movie ko represent karta hai (title, year, director, duration) |
| `TVSeries` | `Movie` se inherit karta hai — TV series ke liye extra info (seasons, episodes) |
| `MediaCatalogue` | Movies aur Series ko store karne wala catalogue |

---

## 🧩 Class-by-Class Breakdown

### 1. `MediaError`
Ye ek **custom exception class** hai jo Python ke built-in `Exception` se inherit hoti hai.

```python
class MediaError(Exception):
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj
```

- `message` → error ka text
- `obj` → wo object jis ki wajah se error aayi

Iska faida ye hai ke error ke sath sath, aapko ye bhi pata chal jata hai ke **konsa object problem create kar raha tha**.

---

### 2. `Movie` (Parent Class)

Ye class ek single movie ko represent karti hai.

```python
Movie(title, year, director, duration)
```

**Validation checks** (agar galat data diya to `ValueError` aayega):
- ✅ Title empty nahi honi chahiye
- ✅ Year 1895 ya usse zyada honi chahiye (pehli movie 1895 mein bani thi 🎥)
- ✅ Director ka naam empty nahi hona chahiye
- ✅ Duration positive number honi chahiye

`__str__` method ek readable format mein movie print karti hai:
```
The Matrix (1999) - 136 min, The Wachowskis
```

---

### 3. `TVSeries` (Child Class — inherits from `Movie`)

Ye class `Movie` se **inherit** karti hai, matlab isko wo saari properties automatically mil jati hain (title, year, director, duration), aur do extra cheezein add hoti hain:

```python
TVSeries(title, year, director, duration, seasons, total_episodes)
```

- `seasons` → kam se kam 1 hona chahiye
- `total_episodes` → kam se kam 1 hona chahiye
- `duration` yahan **average episode length** ke tor pe use hoti hai

`super().__init__()` ka use karke parent class (`Movie`) ka constructor call kiya jata hai — isse code repeat nahi hota.

Output format:
```
Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
```

---

### 4. `MediaCatalogue`

Ye class Movies aur TV Series dono ko ek `list` mein store karti hai.

#### Important Methods:

| Method | Kaam |
|---|---|
| `add(media_item)` | Catalogue mein item add karta hai (sirf `Movie` ya `TVSeries` allow hai) |
| `get_movies()` | Sirf pure `Movie` objects return karta hai (TVSeries nahi) |
| `get_tv_series()` | Sirf `TVSeries` objects return karta hai |
| `__str__` | Poore catalogue ko organized format mein print karta hai |

#### 🔍 Ek zaroori detail — `type()` vs `isinstance()`

```python
def get_movies(self):
    return [item for item in self.items if type(item) is Movie]
```
Yahan `type(item) is Movie` use hua hai — ye sirf **exact** `Movie` objects match karega, `TVSeries` nahi (kyunke `TVSeries` bhi technically ek `Movie` hi hoti hai, inheritance ki wajah se).

```python
def get_tv_series(self):
    return [item for item in self.items if isinstance(item, TVSeries)]
```
Yahan `isinstance()` use hua — ye `TVSeries` aur uski koi bhi subclass match karega.

**Yaad rakhne wali baat:** `isinstance()` inheritance ko follow karta hai, `type() is` nahi karta.

---

## ⚙️ Error Handling

Program ke end mein `try/except` block hai jo do tarah ke errors handle karta hai:

```python
try:
    # movies aur series add karna
except ValueError as e:
    print(f'Validation Error: {e}')
except MediaError as e:
    print(f'Media Error: {e}')
```

- `ValueError` → jab data invalid ho (e.g., empty title, negative duration)
- `MediaError` → jab koi non-Movie/TVSeries object catalogue mein add karne ki koshish ki jaye

---

## ▶️ Sample Output

Jab ye code run hota hai to output kuch is tarah aata hai:

```
Media Catalogue (4 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Inception (2010) - 148 min, Christopher Nolan
=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
2. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

---

## 🚀 How to Run

```bash
python media_catalogue.py
```

Python 3.6+ chahiye hoga (f-strings use hui hain).

---

## 💡 Key OOP Concepts Used

- **Inheritance** — `TVSeries` extends `Movie`
- **Encapsulation** — validation logic constructor ke andar
- **Custom Exceptions** — `MediaError`
- **Polymorphism** — `__str__` har class mein alag behave karta hai
- **`isinstance()` vs `type()`** — subclass filtering ka farq

---

## 📄 License

Free to use for learning purposes.
