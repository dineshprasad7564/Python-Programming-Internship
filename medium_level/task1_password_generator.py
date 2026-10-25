"""
Medium Level - Task 1: Password Generator
Objective: Generate random data using the random and string modules.

The password is guaranteed to contain letters, numbers,
and special characters, in a length chosen by the user.
"""

import random
import string

print("=" * 35)
print("       PASSWORD GENERATOR")
print("=" * 35)

try:
    length = int(input("Enter the desired password length (minimum 6): "))
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    if length < 6:
        print("Password is too short! Please use at least 6 characters.")
    else:
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        # Guarantee at least one character from each category.
        password_chars = [
            random.choice(letters),
            random.choice(digits),
            random.choice(symbols),
        ]

        # Fill the remaining length from all characters combined.
        all_chars = letters + digits + symbols
        password_chars += [random.choice(all_chars) for _ in range(length - 3)]

        # Shuffle so the guaranteed characters are not always at the start.
        random.shuffle(password_chars)
        password = "".join(password_chars)

        print(f"\nYour generated password is:\n{password}")
