# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
tuple1 = tuple(range(1, 11))
print(tuple1)

# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(tuple2))

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
tuple3 = ('a', 'b', 'c', 'd', 'e')
print(tuple3[2])

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
tuple4 = (23, 45, 12, 67, 34, 89, 56)
print(max(tuple4))

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
tuple5 = (1, 5, 2, 5, 3, 5, 4, 5, 6)
print(tuple5.count(5))

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
tuple6 = (10, 3.14, "hello", True)
print(tuple6)

# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
tuple7 = ('java', 'python', 'c++', 'javascript')
print(tuple7.index('python'))

# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
tuple8 = (10, 20, 30, 40, 50)
print(25 in tuple8)


# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
tuple9 = tuple(range(2, 11, 2))
print(tuple9)

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")

tuple10 = (15, 23, 31, 42, 56, 78)
average = sum(tuple10) / len(tuple10)
print(average)
