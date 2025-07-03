#you can use all this modules
#date time module
#stripe method
#split method
#formate method

"""Build a python-based personal expense tracker with file storage
which include features
add new expenses(date,category, description,amount)

View all expenses
Search/ file in csv expense by category or date
Store data in csv file for persistence
Project structure

expense_tracker/
expense_tracker.py
expenses.csv
"""

import os
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize CSV file with header if not present
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            file.write("Date,Category,Description,Amount\n")

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    category = input("Enter category (e.g., Food, Travel, etc.): ").strip()
    description = input("Enter description: ").strip()
    amount = input("Enter amount: ").strip()

    try:
        amount_float = float(amount)  # Validate amount
    except ValueError:
        print("❌ Invalid amount.")
        return

    with open(FILENAME, "a") as file:
        file.write(f"{date},{category},{description},{amount_float:.2f}\n")
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    if not os.path.exists(FILENAME):
        print("❌ Expense file not found.")
        return

    print("\n📄 All Expenses:\n")
    print("{:<12} {:<15} {:<30} {:>10}".format("Date", "Category", "Description", "Amount"))
    print("-" * 70)

    with open(FILENAME, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                date, category, description, amount = parts
                print("{:<12} {:<15} {:<30} Rs{:>7}".format(date, category, description, amount))

# Search expenses by category or date
def search_expenses():
    if not os.path.exists(FILENAME):
        print("❌ No expenses file found.")
        return

    choice = input("Search by (1) Date or (2) Category? ").strip()
    keyword = input("Enter value to search: ").strip().lower()
    found = False

    print("\n🔍 Matching Expenses:\n")
    print("{:<12} {:<15} {:<30} {:>10}".format("Date", "Category", "Description", "Amount"))
    print("-" * 70)

    with open(FILENAME, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                date, category, description, amount = parts
                if (choice == '1' and date == keyword) or (choice == '2' and category.lower() == keyword):
                    print("{:<12} {:<15} {:<30} Rs{:>7}".format(date, category, description, amount))
                    found = True

    if not found:
        print("❌ No matching expenses found.")

# Main menu
def main():
    initialize_file()
    while True:
        print("\n💸 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_expenses()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option, please try again.")

# Correct entry point
if __name__ == "__main__":
    main()
