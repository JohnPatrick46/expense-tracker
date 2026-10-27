#Expense Tracker Installment 4: The Tracker Makes Decisions
#Author: John Patrick B. Escandor
#Tracker wants to help users to save money.

print("=" * 40)
print("EXPENSE TRACKER".center(40))
print("Be Smart, Save Smart".center(40))
print("=" * 40)

print("MAIN MENU")
print("[1] Add Expense".center(20)+"\t\t(coming soon)")
print("[2] View Expenses".center(21)+"\t\t(coming soon)")
print("[3] Show Total Spent".center(23)+"\t\t(coming soon)")
print("[4] Exit".center(11)+"\t\t\t(coming soon)\n")

name = input("What's your name? ")
print (f"Welcome {name}! Let's log two expenses.\n")

subtotal = 0
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

if amount1 > 200:
    print("Huge expense - are you sure?")
elif amount1 > 100:
    print("Big expense.")
elif amount1 > 50:
    print("Moderate expense.")
else:
    print("Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

if amount2 > 200:
    print("Huge expense - are you sure?")
elif amount2 > 100:
    print("Big expense.")
elif amount2 > 50:
    print("Moderate expense.")
else:
    print("Small expense.")

if amount1 > 100 and amount2 > 100:
    print("Two big expenses in a row - slow down!")

tax_percent = int(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print("\n", "-" * 40, sep="")
print("SUMMARY")
print(f"\N{SPACE}-\N{SPACE}{item1 + ':':<13}${amount1}")
print(f"\N{SPACE}-\N{SPACE}{item2 + ':':<13}${amount2}")
print(f"{'Subtotal:':<16}${subtotal}")
print(f"{'Average:':<16}${average}")
print(f"{f'Tax ({tax_percent:.1f}%):':<16}${tax:.1f}")
print(f"{'Grand total:':<16}${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)

print("Made by: John Patrick B. Escandor | Installment 4")