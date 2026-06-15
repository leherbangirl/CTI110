# Lauren Thomas
# June 15, 2026
# P1HW2
# This program calculates travel expenses and remaining budget.

# Ask the user for their budget.
# Ask the user for their travel destination.
# Ask the user for gas expenses.
# Ask the user for accommodation expenses.
# Ask the user for food expenses.
# Add all expenses together.
# Subtract expenses from the budget.
# Display the travel destination, budget, expenses, and remaining balance.

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

expenses = gas + accommodation + food
remaining_balance = budget - expenses

print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("\nRemaining Balance:", remaining_balance)