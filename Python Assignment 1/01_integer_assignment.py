# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
A = 5
for i in range(5, 14):
    A *= i
print("A of first 10 natural numbers is:", A)


# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")

remainder = 156 % 7
print(remainder)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")

square = 25 ** 2
print(square)

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")

cube_root = 125**(1/3)
print(cube_root)

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")

numbers = 12345
digit_sum = sum(int(digit) for digit in str(numbers))
print(digit_sum)

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")

n = 97
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
print("Prime" if is_prime else "Not Prime")

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")

factorial = 1
for i in range(1, 9):
    factorial *= i
print(factorial)

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")

total = 15 + 23 + 31 + 42 + 56
count = 5
average = total / count
print(average)

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")

import math
gcd_value = math.gcd(48, 36)
print(gcd_value)

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")

odd_sum = 0
for i in range(20):
    odd_sum += 2 * i + 1
print(odd_sum)
