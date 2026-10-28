#Expense Tracker Installment 5: The Menu Comes Alive
#Author: John Patrick B. Escandor
#Tracker allows user to choose what to do and gives feedback.

print("=" * 40)
print("EXPENSE TRACKER".center(40))
print("Be Smart, Save Smart".center(40))
print("=" * 40)

name = input("What's your name? ")
tax_percent = int(input("Tax rate %? "))
budget = float(input("Your budget? "))

subtotal = 0
count = 0
choice = ""

print (f"Welcome, {name}!")

while choice != "4":
    print("\nMAIN MENU")
    print("1. Add Expense")
    print("2. View Expenses (coming soon)")
    print("3. Show Total Spent")
    print("4. Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount1 = float(input("Amount? "))
        subtotal = subtotal + amount1
        count += 1

        if amount1 > 200:
            print("\N{SPACE}Huge expense - are you sure?")
        elif amount1 > 100:
            print("\N{SPACE}Big expense.")
        elif amount1 > 50:
            print("\N{SPACE}Moderate expense.")
        else:
            print("\N{SPACE}Small expense.")

    elif choice == "2":
        print("\N{SPACE}Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total

        print(f"\N{SPACE}{'Expenses:':<16}{count}")
        print(f"\N{SPACE}{'Subtotal:':<16}${subtotal:.1f}")
        print(f"\N{SPACE}{f'Tax ({tax_percent:.1f}%):':<16}${tax:.1f}")
        print(f"\N{SPACE}{'Grand total:':<16}${total:.1f}")

        if over_budget:
            print(f"\N{SPACE}Over budget by ${total - budget:.1f}!")
        elif total > budget * 0.9:
            print(f"\N{SPACE}Careful: only ${left:.1f} left.")
        else:
            print(f"\N{SPACE}Within budget. ${left:.1f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)

    else:
        print(f"\N{SPACE}Please choose 1, 2, 3 or 4.")

print("Made by: John Patrick B. Escandor | Installment 5")
print("=" * 40)