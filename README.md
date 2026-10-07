# Personal Mini-Toolkit (PLP Python Week 8 Final Project)

A versatile, menu-driven Python application demonstrating core concepts: variables, user input/output, conditionals, loops, lists, functions, and error handling.

## Featured Tools
1. Quick Calculator: Performs basic math (+, -, *, /) with zero-division protection.
2. Interactive To-Do List: Dynamically manages tasks (view, add, remove) using Python lists.
3. Number Guessing Game: A game featuring attempt tracking and randomized numbers.

## How to Run
Ensure Python 3 is installed, then execute: python toolkit.py

## Reflection
Building this project was a rewarding culmination of the foundational Python course. The hardest part was managing state for the To-Do list so tasks stayed intact when moving in and out of the tool menu. The trickiest bug happened when removing tasks by index—handling off-by-one errors and invalid integer inputs required careful try/except blocks. If I had one more week, I would add file I/O using Python's json module to persist to-do items to a local file between program executions.
