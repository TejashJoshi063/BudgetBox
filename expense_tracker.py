from expense import Expense
import csv

# 1. Main Project structure
def main():
    print("🎯 Running Expense Tracker!")
    expense_file_path = "expense.csv"

    # Ask user for their total budget
    while True:
        try:
            budget = float(input("Enter your total budget for expenses: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create a loop for the user menu
    while True:
        print("\nSelect an option:")
        print("1. Add a new expense")
        print("2. View expense summary and exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Add a new expense
            expense = get_user_expense()
            save_expense_to_file(expense, expense_file_path)
            print("Expense added successfully!")
        elif choice == '2':
            # View summary and exit
            summarize_expenses(expense_file_path, budget)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# 2. Saving their Expense to a file
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    try:
        with open(expense_file_path, "a", newline="") as f:  # Using "a" for open file in append mode
            writer = csv.writer(f)
            writer.writerow([expense.name, expense.amount, expense.category])
    except PermissionError:
        print(f"Error: Permission denied to write to '{expense_file_path}'.")
        print("Please make sure the file is not open in another program (like Excel).")


def get_user_expense():
    print("Getting User Expense")
    # 3. Getting user Expenses
    expense_name = input("Enter Expense name:")
    while True:
        try:
            expense_amount = float(input("Enter Expense amount:"))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]
    # Create a loop to let the user select an expense category
    while True:
        print("Select a Category")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1} . {category_name}")
        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
                return new_expense
            else:
                print("Invalid category. Please try again!")
        except ValueError:
            print("Invalid input. Please enter a number.")

#4. Summarizing Expenses to a file
def summarize_expenses(expense_file_path, budget):
    print("Summarizing User Expense")
    expenses: list[Expense] = []
    try:
        with open(expense_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                expense_name, expense_amount, expense_category = stripped_line.split(",")
                line_expense = Expense(
                    name=expense_name,
                    amount=float(expense_amount),
                    category=expense_category,
                )
                expenses.append(line_expense)
    except FileNotFoundError:
        print("No expenses file found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    if not expenses:
        print("No expenses to summarize.")
        return

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("\n--- Expense Summary ---")
    print("Expenses by category:")
    for key, amount in sorted(amount_by_category.items()):
        print(f"  {key}: ${amount:.2f}")

    total_expense = sum(ex.amount for ex in expenses)
    print(f"\nTotal Expense: ${total_expense:.2f}")
    print(f"Budget: ${budget:.2f}")
    print(f"Remaining Budget: ${budget - total_expense:.2f}")
    print("-----------------------\n")

if __name__ == "__main__":
    main() 