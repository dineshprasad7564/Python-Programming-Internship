"""
Easy Level - Task 3: Multiplication Table Generator
Objective: Learn how to use loops in Python.

The program prints the multiplication table (1 to 10)
of any number entered by the user.
"""

print("=" * 35)
print("   MULTIPLICATION TABLE GENERATOR")
print("=" * 35)

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a whole number.")
else:
    print(f"\nMultiplication Table of {number}:")
    print("-" * 25)
    for i in range(1, 11):
        print(f"{number} x {i:2d} = {number * i}")
