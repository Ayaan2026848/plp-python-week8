import random

def quick_calculator():
    """Tool 1: A simple calculator using conditionals and f-strings."""
    print("\n--- Tool 1: Quick Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Choose operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print(f"Invalid operation '{op}'. Please use +, -, *, or /.")
            return

        print(f"Result: {num1} {op} {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

def todo_list_manager(tasks):
    """Tool 2: Interactive To-Do List using a list that changes during execution and loops."""
    while True:
        print("\n--- Tool 2: To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Back to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            if not tasks:
                print("Your to-do list is currently empty!")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
        elif choice == '2':
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added task: '{new_task}'")
            else:
                print("Task cannot be blank!")
        elif choice == '3':
            if not tasks:
                print("No tasks available to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed task: '{removed}'")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

def number_guessing_game():
    """Tool 3: Number guessing game using loops, conditionals, and random number generation."""
    print("\n--- Tool 3: Number Guessing Game ---")
    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print(f"I'm thinking of a number between 1 and 20. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if guess == secret:
                print(f"Congratulations! You guessed the secret number {secret} in {attempts} attempts!")
                return
            elif guess < secret:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print(f"Game over! The secret number was {secret}.")

def main():
    """Main program entry point with menu loop and graceful invalid choice handling."""
    print("==================================================")
    print(" Welcome to the Personal Mini-Toolkit Program! ")
    print("==================================================")

    to_do_items = []

    while True:
        print("\n====================================")
        print("         PERSONAL MINI-TOOLKIT       ")
        print("====================================")
        print("1. Quick Calculator")
        print("2. Interactive To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")
        print("------------------------------------")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            quick_calculator()
        elif choice == '2':
            todo_list_manager(to_do_items)
        elif choice == '3':
            number_guessing_game()
        elif choice == '4':
            print("\nThank you for using the Personal Mini-Toolkit! Goodbye!")
            break
        else:
            print(f"'{choice}' is not a valid menu option. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
