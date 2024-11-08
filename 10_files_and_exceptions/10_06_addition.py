# 10-6. Addition
# Write a program that prompts for two numbers.
print("Give me two numbers, and I'll add them.")
    
first_number = input("\nFirst number: ")
second_number = input("Second number: ")
# Catch the ValueError if either input value is not a number.
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    # Print a friendly error message.
    print("Error! Strings cannot be added to numbers.")
else:
    print(answer)

# Test this program by entering two numbers.
# And then by entering some text instead of a number.