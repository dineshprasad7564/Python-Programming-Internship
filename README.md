# Python Programming Internship Tasks

**Intern:** Dinesh Prasad
**Program:** Python Programming Internship

This repository contains my submission for the Python Programming Internship tasks.
As per the task selection rules, I completed **3 tasks from the Easy level, 2 tasks
from the Medium level, and 1 task from the Hard level**. Every program was written in
Python 3 using only the standard library, and all of them were tested successfully.

## Tasks Completed

| Level  | Task | File | Status |
|--------|------|------|--------|
| Easy   | Task 1: Simple Calculator Program | [easy_level/task1_simple_calculator.py](easy_level/task1_simple_calculator.py) | ✅ Completed |
| Easy   | Task 2: Number Guessing Game | [easy_level/task2_number_guessing_game.py](easy_level/task2_number_guessing_game.py) | ✅ Completed |
| Easy   | Task 3: Multiplication Table Generator | [easy_level/task3_multiplication_table.py](easy_level/task3_multiplication_table.py) | ✅ Completed |
| Medium | Task 1: Password Generator | [medium_level/task1_password_generator.py](medium_level/task1_password_generator.py) | ✅ Completed |
| Medium | Task 3: Contact Book Program | [medium_level/task3_contact_book.py](medium_level/task3_contact_book.py) | ✅ Completed |
| Hard   | Task 1: Command Line To-Do List Application | [hard_level/task1_todo_list.py](hard_level/task1_todo_list.py) | ✅ Completed |

Real outputs captured while testing every program are saved in the
[sample_outputs](sample_outputs) folder, proving that each program runs successfully.

## Project Structure

```
Python-Programming-Internship/
├── easy_level/
│   ├── task1_simple_calculator.py
│   ├── task2_number_guessing_game.py
│   └── task3_multiplication_table.py
├── medium_level/
│   ├── task1_password_generator.py
│   └── task3_contact_book.py
├── hard_level/
│   └── task1_todo_list.py
├── sample_outputs/          # Output captured from actual program runs
└── README.md
```

## How to Run

You only need **Python 3** installed — no external libraries are required.

```bash
# Example: run the calculator
python easy_level/task1_simple_calculator.py

# Run any other program the same way, e.g.
python easy_level/task2_number_guessing_game.py
python medium_level/task1_password_generator.py
python hard_level/task1_todo_list.py
```

Each program is interactive: it asks for input in the terminal and displays the result.

## Task Explanations

### Easy Level

**Task 1 — Simple Calculator:** Asks the user for two numbers and a choice of
operation (addition, subtraction, multiplication, division). It uses `if-else`
statements to perform the selected operation. Invalid numbers and division by zero
are handled gracefully.

```text
Enter the first number: 8
Enter the second number: 2
Enter your choice (1/2/3/4): 1
Result: 8.0 + 2.0 = 10.0
```

**Task 2 — Number Guessing Game:** The computer picks a random number between 1 and
100 using the `random` module. The user keeps guessing inside a `while` loop and gets
"Too High" / "Too Low" hints until the number is found. The game counts attempts and
offers to play again.

```text
I have picked a number between 1 and 100. Can you guess it?
Enter your guess: 50
Too Low! Try again.
Enter your guess: 94
Congratulations! You guessed it in 94 attempts.
```

**Task 3 — Multiplication Table Generator:** Asks for a number and uses a `for` loop
to print its multiplication table from 1 to 10.

```text
Enter a number: 7
7 x  1 = 7
7 x  2 = 14
...
7 x 10 = 70
```

### Medium Level

**Task 1 — Password Generator:** Uses the `random` and `string` modules to build a
password of the user's chosen length. The password always contains at least one
letter, one number, and one special character, and the characters are shuffled so
the result looks completely random.

```text
Enter the desired password length (minimum 6): 14
Your generated password is:
||S201h^MI>_]y
```

**Task 3 — Contact Book:** A menu-driven contact manager that stores contacts in a
dictionary (name → phone/email). The user can add, view, and search contacts.

```text
Name                Phone          Email
-----------------------------------------------------------------
Dinesh              9876543210     dinesh@example.com
Priya               9123456780     priya@example.com
```

### Hard Level

**Task 1 — Command Line To-Do List Application:** A complete task manager with a
menu to add, view, and delete tasks. Tasks live in a list during the session and are
saved to `tasks.json` after every change, so the to-do list survives even after the
program is closed.

```text
===== YOUR TASKS =====
1. Buy groceries
2. Finish internship report
3. Read a book
```

## What I Learned

- Working with **variables, conditions, loops, and user input** (Easy tasks)
- **File handling, JSON data storage, and automation** with the `random` and
  `string` modules (Medium/Hard tasks)
- Building complete **menu-driven command-line applications**
- Handling errors gracefully with `try/except` instead of letting programs crash
- Structuring a project with a clear folder layout and documenting it in a README
