# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
print("Python Programming"[::-1])

# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
s = "racecar"
print(s == s[::-1])

# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
print(len("Python is a great programming language".split()))

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
print("Hello World")

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
print(len("Data Science"))

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
print("Machine Learning".replace(" ", "_"))

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
print("python" in "Python Programming Language".lower())

# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
print("Artificial Intelligence"[:5])

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
print("UPPERCASE".lower())

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
s = "Computer Science"
print(''.join(ch for ch in s if ch.lower() not in "aeiou"))

# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
from collections import Counter
print(Counter("mississippi").most_common(1)[0][0])

# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
print(sorted("listen") == sorted("silent"))

# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
print("python programming language".title())

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
s = "Hello World"
print(sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in s))

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
words = "Python is a programming language".split()
print(max(words, key=len))

# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
import string
s = "Hello, World! How are you?"
print(''.join(ch for ch in s if ch not in string.punctuation))

# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
print("Python Programming".startswith("Python"))

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
print("Hello World".find("o"))

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
print("apple,banana,orange".split(","))

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
print(" ".join(['Python', 'is', 'awesome']))

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
print("12345".isdigit())

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
print("HelloWorld".isalpha())

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
s = "hello world"
print(''.join(ch.upper() if i%2 else ch.lower() for i, ch in enumerate(s)))

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
s = "banana"
print([i for i, ch in enumerate(s) if ch == 'a'])

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
print("  Hello World  ".strip())

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
print("programming".endswith("ing"))

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
print("Hello World".replace("o", "0", 1))

# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
words = "Python is a programming language".split()
print(min(words, key=len))

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
words = "Python programming is powerful".lower().split()
print(sum(w.startswith("p") for w in words))

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
print(" ".join("Hello World Python".split()[::-1]))56;pn/.3d1234567890

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
import re
print(bool(re.match(r"[^@]+@[^@]+\.[^@]+", "user@example.com")))

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
url = "https://www.example.com/path"
print(url.split("/")[2])

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
s = """line1
line2
line3"""
print(len(s.splitlines()))

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
print(set("hello") & set("world"))

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
print(bool(re.match(r"^\+?\d{1,3}-\d{3}-\d{3}-\d{4}$", "+1-555-123-4567")))

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
print(re.findall(r"\d+", "abc123def456ghi789"))

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
s = "snake_case"
parts = s.split("_")
print(parts[0] + "".join(p.title() for p in parts[1:]))

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
s = "A man a plan a canal Panama"
clean = ''.join(ch.lower() for ch in s if ch.isalnum())
print(clean == clean[::-1])

# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
from collections import Counter
words = "the quick brown fox jumps over the lazy dog".split()
print(Counter(words).most_common(1)[0][0])

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
s = "National Aeronautics and Space Administration"
print(''.join(w[0].upper() for w in s.split()))

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
s = "((()))"
count = 0
balanced = True

for ch in s:
    if ch == "(":
        count += 1
    elif ch == ")":
        count -= 1
    if count < 0:  # More closing than opening
        balanced = False
        break

if count != 0:
    balanced = False

print(balanced)

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....',
         'i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.',
         'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
         'y':'-.--','z':'--..',' ':'/'}
s = "hello world"
print(' '.join(morse[ch] for ch in s))

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[""]*(n+1) for _ in range(m+1)]
    longest = ""
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + s1[i-1]
                if len(dp[i][j]) > len(longest):
                    longest = dp[i][j]
    return longest
print(lcs("programming", "grammar"))

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
import re
print(bool(re.match(r"^https?://[^\s]+$", "https://www.google.com")))

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
words = "Python programming is amazing and powerful".split()
print([w for w in words if len(w) > 5])

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
def pig_latin(word):
    return word[1:] + word[0] + "ay"
print(' '.join(pig_latin(w) for w in "hello world".split()))

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
import re
print(bool(re.match(r"^(\d{1,3}\.){3}\d{1,3}$", "192.168.1.1")))

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
s = "abc"
subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
print(subs)

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
import codecs
print(codecs.encode("hello world", "rot_13")) Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")

def luhn(card):
    digits = [int(x) for x in card]
    for i in range(len(digits)-2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0
print(luhn("4532015112830366")) 
