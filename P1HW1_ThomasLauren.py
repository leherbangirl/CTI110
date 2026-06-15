# Lauren Thomas
# June 15, 2026
# P1HW1
# This program calculates exponents and performs addition and subtraction.

print("-----Calculating Exponents-----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()
print(base, "raised to the power of", exponent, "is", result, "!!")
print()

print("-----Addition and Subtraction-----")
print()

starting_integer = int(input("Enter a starting integer: "))
add_integer = int(input("Enter an integer to add: "))
subtract_integer = int(input("Enter an integer to subtract: "))

total = starting_integer + add_integer - subtract_integer

print()
print(starting_integer, "+", add_integer, "-", subtract_integer, "is equal to", total)