#Expense Tracker Installment 2: Talking to the User
#Author: John Patrick B. Escandor
#Basic Upgrade on the Expense Tracker, we will be communicating with the user.

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("\n","-" * 40, sep="")
print("SUMMARY")
print(f"- {item1}:\t${amount1}".center(18," "))
print(f"- {item2}:\t${amount2}".center(17," "))
print(f"Total Spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)

print("Made by: John Patrick B. Escandor | Installment 2")