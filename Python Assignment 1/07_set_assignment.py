# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
natural_set = set(range(1, 11))
print(natural_set)

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
s = {1, 2, 3, 4, 5}
s.add(11)
print(s)

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
s = {1, 2, 3, 4, 5, 6}
s.remove(3)
print(s)

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.intersection(b))

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
print(a.difference(b))

# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
s = {1, 2, 3, 4, 6, 7, 8}
print(5 in s)

# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
s = {'a', 'b', 'c', 'd', 'e'}
print(len(s))

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
vowels = {'a', 'e', 'i', 'o', 'u'}
string = "hello world"
vowel_set = set([ch for ch in string if ch in vowels])
print(vowel_set)

# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] usi
