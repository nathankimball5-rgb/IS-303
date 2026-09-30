import math
from statistics import mean

expense = 1
small_expenses = 0
moderate_expenses = 0
large_expenses = 0

all_expenses = []

while expense != 0:

    #Tell the user to input the expenses that they have and add them into the list. 
    expense = float(input("Enter an expense or 0 to finish: "))
    while expense < 0:
        print("Please enter a response greater than 0")
        expense = float(input("Enter an expense or 0 to finish: "))
    #Making sure that we aren't counting 0 as an expense.
    if expense != 0:
        all_expenses.append(expense)
#loop

#Classifying expenses i is < 25 count as small expense, >= 25 and <=100 moderate expense, and then > 100 large expense. 
for i in all_expenses:
    if i < 25:
        small_expenses += 1
    elif i >= 25 and i <= 100:
        moderate_expenses += 1
    elif i > 100:
        large_expenses += 1
#end of if statement

#setting variables to get the proper amounts. 
amount_expenses = len(all_expenses)
total = math.fsum(all_expenses)
average_amount = mean(all_expenses)
smallest_expense = min(all_expenses)
largest_expense = max(all_expenses)

#print out output for user to see. 
print()
title = "Expense Summary"
print(title)
print("-" * len(title))

print(f"Number of expenses: {amount_expenses}")
print("Total: ${:,.2f}".format(total))
print("Average: ${:,.2f}".format(average_amount))
print("Smallest expense: ${:,.2f}".format(smallest_expense))
print("Largest expense: ${:,.2f}".format(largest_expense))
print()

print(f"Small expenses: {small_expenses}")
print(f"Moderate expenses: {moderate_expenses}")
print(f"Large expenses: {large_expenses}")


