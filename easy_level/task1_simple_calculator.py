"""
Easy Level - Task 1: Simple Calculator Program
Objective: Perform basic arithmetic operations using Python.

The program asks the user for two numbers and an operation,
then uses if-else statements to calculate and display the result.
"""


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


print("=" * 35)
print("         SIMPLE CALCULATOR")
print("=" * 35)

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ").strip()

if choice == "1":
    print(f"\nResult: {num1} + {num2} = {num1 + num2}")
elif choice == "2":
    print(f"\nResult: {num1} - {num2} = {num1 - num2}")
elif choice == "3":
    print(f"\nResult: {num1} * {num2} = {num1 * num2}")
elif choice == "4":
    if num2 == 0:
        print("\nError: Division by zero is not allowed!")
    else:
        print(f"\nResult: {num1} / {num2} = {num1 / num2}")
else:
    print("\nInvalid choice! Please select 1, 2, 3, or 4.")
