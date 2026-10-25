"""
Easy Level - Task 2: Number Guessing Game
Objective: Understand how loops and conditions work in Python.

The computer picks a random number between 1 and 100.
The user keeps guessing until they find it, getting
"Too High" / "Too Low" hints along the way.
"""

import random


def play_game():
    """Run one round of the guessing game and return the number of attempts."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have picked a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            return attempts


print("=" * 35)
print("      NUMBER GUESSING GAME")
print("=" * 35)

total_rounds = 0

while True:
    play_game()
    total_rounds += 1
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        print(f"\nThanks for playing! You completed {total_rounds} round(s).")
        break
