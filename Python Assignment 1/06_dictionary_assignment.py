# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1:")
students = {"Alice": 20, "Bob": 22, "Charlie": 19}
print(students)

# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2:")
d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 4
print(d)

# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3:")
d = {'name': 'John', 'age': 25, 'city': 'New York'}
print(list(d.keys()))

# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4:")
d = {'python': 3, 'java': 2, 'c++': 1}
print(list(d.values()))

# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5:")
d = {'name': 'Alice', 'age': 30, 'city': 'London'}
print('age' in d)

# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6:")
d = {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
d.pop('temp')
print(d)

# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7:")
d = {'math': 85, 'science': 92, 'english': 78}
print(sum(d.values()))

# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8:")
squares = {i: i**2 for i in range(1, 6)}
print(squares)

# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9:")
word = "hello"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}
print("\nQuestion 10:")
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = {**d1, **d2}
print(merged)

# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11:")
nested = {'person': {'name': 'Alice', 'age': 25}}
print(nested)

# Question 12: Access nested value 'name'
print("\nQuestion 12:")
print(nested['person']['name'])

# Question 13: Dictionary with list values
print("\nQuestion 13:")
d = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print(d)

# Question 14: Add 'orange' to fruits
print("\nQuestion 14:")
d['fruits'].append('orange')
print(d)

# Question 15: Dictionary with tuple values
print("\nQuestion 15:")
d = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print(d)

# Question 16: Extract first coordinate
print("\nQuestion 16:")
print(d['coordinates'][0])

# Question 17: Dictionary with set values
print("\nQuestion 17:")
d = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print(d)

# Question 18: Add 'o' to vowels
print("\nQuestion 18:")
d['vowels'].add('o')
print(d)

# Question 19: 3-level nested dictionary
print("\nQuestion 19:")
d = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print(d)

# Question 20: Access employee name
print("\nQuestion 20:")
print(d['company']['department']['employee']['name'])

# Question 21: Mixed data types
print("\nQuestion 21:")
d = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print(d)

# Question 22: Data types of values
print("\nQuestion 22:")
for k, v in d.items():
    print(k, type(v))

# Question 23: Dictionary with function values
print("\nQuestion 23:")
d = {'len': len, 'str': str, 'int': int}
print(d)

# Question 24: Apply each function to '123'
print("\nQuestion 24:")
print(d['len']("123"))
print(d )
print(d['int']("123"))

# Question 25: Dictionary with lambda functions
print("\nQuestion 25:")
d = {'double': lambda x: x*2, 'square': lambda x: x**2}
print(d)

# Question 26: Apply each lambda function to 5
print("\nQuestion 26:")
print(d )
print(d )

# Question 27: Dictionary with class values
print("\nQuestion 27:")
d = {'list': list, 'dict': dict, 'set': set}
print(d)

# Question 28: Create instances
print("\nQuestion 28:")
print(d['list']([1,2,3]))
print(d['dict'](a=1, b=2))
print(d['set']([1,2,2,3]))

# Question 29: Dictionary with None values
print("\nQuestion 29:")
d = {'a': None, 'b': None, 'c': None}
print(d)

# Question 30: Replace all None with 0
print("\nQuestion 30:")
d = {k: (0 if v is None else v) for k, v in d.items()}
print(d)

# Question 31: Boolean dictionary
print("\nQuestion 31:")
d = {'is_active': True, 'is_admin': False}
print(d)

# Question 32: Count True values
print("\nQuestion 32:")
print(sum(v for v in d.values()))

# Question 33: Complex numbers dictionary
print("\nQuestion 33:")
d = {'z1': 3+4j, 'z2': 1+2j}
print(d)

# Question 34: Magnitude of complex numbers
print("\nQuestion 34:")
print(abs(d['z1']), abs(d['z2']))

# Question 35: 4-level nested dictionary
print("\nQuestion 35:")
d = {'a': {'b': {'c': {'d': 100}}}}
print(d)

# Question 36: Access deepest value
print("\nQuestion 36:")
print(d['a']['b']['c']['d'])

# Question 37: Dictionary with ranges
print("\nQuestion 37:")
d = {'r1': range(3), 'r2': range(5)}
print(d)

# Question 38: Convert each range to list
print("\nQuestion 38:")
print({k: list(v) for k,v in d.items()})

# Question 39: Dictionary with generators
print("\nQuestion 39:")
d = {'gen1': (x for x in range(3)), 'gen2': (y*y for y in range(4))}
print(d)

# Question 40: Convert each generator to list
print("\nQuestion 40:")
print({k: list(v) for k,v in d.items()})

# Question 41: Dictionary with iterators
print("\nQuestion 41:")
d = {'iter1': iter([1,2,3]), 'iter2': iter("abc")}
print(d)

# Question 42: Extract elements from iterators
print("\nQuestion 42:")
print({k: list(v) for k,v in d.items()})

# Question 43: Nested lists dictionary
print("\nQuestion 43:")
d = {'matrix': [[1,2],[3,4]], 'vector': [5,6,7]}
print(d)

# Question 44: Sum of nested lists
print("\nQuestion 44:")
print({k: sum(map(sum,v)) if isinstance(v[0], list) else sum(v) for k,v in d.items()})

# Question 45: Nested dictionaries
print("\nQuestion 45:")
d = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print(d)

# Question 46: Access db port
print("\nQuestion 46:")
print(d['config']['db']['port'])

# Question 47: Nested tuples dictionary
print("\nQuestion 47:")
d = {'points': ((1,2),(3,4)), 'rgb': ((255,0,0),(0,255,0))}
print(d)

# Question 48: First point coordinates
print("\nQuestion 48:")
print(d['points'][0])

# Question 49: Nested sets (use list of sets, since set of set not allowed)
print("\nQuestion 49:")
d = {'groups': [{1,2,3},{4,5,6}], 'categories': [{'a','b'},{'c','d'}]}
print(d)

# Question 50: Union of nested sets
print("\nQuestion 50:")
print({k: set().union(*v) for k,v in d.items()})
