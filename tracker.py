#Expense Tracker Installment 3: The Tracker Does Math
#Author: John Patrick B. Escandor
#Basic Mathematical Upgrade to the Expense Tracker.

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
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

tax_percent = int(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print("\n","-" * 40, sep="")
print("SUMMARY")
print(f"- {item1}:\t${amount1}".center(18," "))
print(f"- {item2}:\t${amount2}".center(17," "))
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent:.1f}%):\t${tax:.1f}")
print(f"Grand total:\t${total}")
print(f"Over budget?:\t${over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

print("Made by: John Patrick B. Escandor | Installment 3")