# Multiples of Ten
# Ask the user for a number
number = input("Please enter a number, and I'll tell you if it's a multiple of 10: ")
number = int(number)

# Report whether the number is a multiple of 10 or not
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")