# COMPLEX DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Create a complex number and find its conjugate
print("SOLVED EXAMPLE:")
print("Create a complex number and find its conjugate")
z = 3 + 4j
conjugate = z.conjugate()
magnitude = abs(z)
print(f"Complex number: {z}")
print(f"Conjugate: {conjugate}")
print(f"Magnitude: {magnitude}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create complex number 5 + 3j
print("Question 1: Create complex number 5 + 3j")
import cmath
z1 = complex(5, 3)
print(z1)

# Question 2: Find the real part of complex number 7 - 2j
print("\nQuestion 2: Find the real part of complex number 7 - 2j")
importh cmath
z2 = complex(7, -2)
print(z2.real)

# Question 3: Find the imaginary part of complex number 4 + 6j
print("\nQuestion 3: Find the imaginary part of complex number 4 + 6j")
import cmath
z3 = complex(4, 6)
print(z3.imag)

# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
print("\nQuestion 4: Add two complex numbers: (3 + 2j) and (1 + 4j)")
import cmath
z4 = complex(3, 2) + complex(1, 4)
print(z4)

# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
print("\nQuestion 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)")
import cmath
z5 = complex(2, 3) * complex(1, 2)
print(z5)

# Question 6: Find the magnitude of complex number 6 + 8j
print("\nQuestion 6: Find the magnitude of complex number 6 + 8j")
import cmath
z6 = complex(6, 8)
print(abs(z6))

# Question 7: Find the conjugate of complex number 5 - 7j
print("\nQuestion 7: Find the conjugate of complex number 5 - 7j")
import cmath
z7 = complex(5, -7)
print(z7.conjugate())

# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
print("\nQuestion 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)")
import cmath
z8 = complex(10, 5) - complex(3, 2)
print(z8)

# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
print("\nQuestion 9: Divide complex numbers: (8 + 6j) / (2 + 1j)")
import cmath
z9 = complex(8, 6) / complex(2, 1)
print(z9)

# Question 10: Find the phase angle of complex number 1 + 1j
print("\nQuestion 10: Find the phase angle of complex number 1 + 1j")
import cmath
z10 = complex(1, 1)
print(cmath.phase(z10))
