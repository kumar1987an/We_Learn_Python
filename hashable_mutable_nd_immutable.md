# What is hashable data types ??

Hashing is the process of converting a given key into another value. A hash function is used to generate the new value according to a mathematical algorithm. The result of a hash function is known as a hash value or simply, a hash.

A simple hashing approach would be to take the modular of the key (assuming it’s numerical) against the table’s size:

```python
index = key % tableSize # i.e tableSize = (len(list))
```

**Hence all immutable objects that is unchangable objects are hashable because its hash value never changes over the course of time**

```python
# Hashable data types: int, float, str, tuple, and None.
# Unhashable data types: dict, list, and set.
```

*Hint - Hashing is also used in data encryption. Passwords can be stored in the form of their hashes so that even if a database is breached, plaintext passwords are not accessible. MD5, SHA-1 and SHA-2 are popular cryptographic hashes.*

```python
# Creates an empty set

elements = set()

# List of objects which is to be added to list

list_items = [
    1,  # int
    7.88,  # float
    "twinkle",  # str
    (1003, 22, 0.2),  # tuple
    {"a": "apple"},  # dict
    [100, 200],  # list
    None,  # None
]
```
```python
>>> elements.add(items[0])
>>> elements.add(items[1])
>>> elements.add(items[2])
>>> elements.add(items[3])
>>> elements.add(items[4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
>>> elements.add(items[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> elements.add(items[6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> elements.add(items[7])
>>> elements
{0.1, 1, 'abc', None, (2, 3)}
```