# Singly Linked List (Python Implementation)

A simple, from-scratch implementation of a **singly linked list** data structure in Python, supporting insertion at the end, removal by value, and an empty-check helper.

## Overview

A linked list is a linear data structure in which elements (called **nodes**) are stored in separate objects, each pointing to the next one in the sequence. Unlike arrays, linked lists do not require contiguous memory and allow efficient insertion/removal without shifting elements.

This implementation provides:

- A `Node` class (nested inside `LinkedList`) representing a single element in the list.
- A `LinkedList` class managing the collection of nodes.

## Class Structure

### `LinkedList.Node`

Represents a single node in the list.

| Attribute | Description |
|-----------|-------------|
| `element` | The value stored in the node |
| `next`    | Reference to the next node in the list (or `None` if it's the last node) |

### `LinkedList`

| Attribute | Description |
|-----------|-------------|
| `length`  | Tracks the total number of elements in the list |
| `head`    | Reference to the first node in the list (or `None` if the list is empty) |

## Methods

### `is_empty()`
Returns `True` if the list has no elements, otherwise `False`.

```python
my_list.is_empty()
```

### `add(element)`
Adds a new element to the **end** of the list.

- If the list is empty, the new node becomes the `head`.
- Otherwise, the method traverses to the last node and attaches the new node after it.
- Time complexity: **O(n)**, since it must walk to the end of the list.

```python
my_list.add(1)
my_list.add(2)
```

### `remove(element)`
Removes the **first node** matching the given value.

- Traverses the list while keeping track of the previous node.
- If the element is not found, the method returns without making changes.
- If the element is found at the head, `head` is updated directly.
- Otherwise, the previous node's `next` pointer is updated to skip over the removed node.
- Time complexity: **O(n)**.

```python
my_list.remove(1)
```

## Example Usage

```python
my_list = LinkedList()
print(my_list.is_empty())   # True

my_list.add(1)
my_list.add(2)
print(my_list.is_empty())   # False
print(my_list.length)       # 2

my_list.remove(1)
print(my_list.length)       # 1
```

## Expected Output

```
True
False
2
1
```

## Time Complexity Summary

| Operation   | Complexity |
|-------------|------------|
| `is_empty()`| O(1)       |
| `add()`     | O(n)       |
| `remove()`  | O(n)       |

## Notes

- This is a **singly** linked list — nodes only point forward, not backward.
- The `add()` method always inserts at the end (tail), not the beginning.
- The `remove()` method removes only the **first occurrence** of the given value.
