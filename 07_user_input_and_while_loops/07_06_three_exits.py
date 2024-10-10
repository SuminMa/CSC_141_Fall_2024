# 7-6. Three Exits
'''
Write different versions of eigher Excercies 7-5 that do each of the following
Use a conditional test in the while statement to stop the loop
Use an active variable to control how long the loop runs
'''

# Use an active variable to control how long the loop runs
count = 0
# Write a loop in which I ask users their age, and then tell them the cost
# Use a conditional test in the while statement to stop the loop
while count <= 10:
    age = input("How old are you? ")
    # Use a break statement to exit the loop when the user enters a 'quit' value
    if age == 'quit':
        break
    else:
        age = int(age)
    # If a person is under the age of 3, the ticket is free
        if age < 3:
            print("The ticket for you is free.")
    # If they are between 3 and 12, the ticket is $10
        elif age >= 3 and age < 12:
            print("The ticket for you would be $10.")
    # If they are over age 12. the ticket is $15
        else:
            print("The ticket for you would be $15.")
        count += 1

print("Thank you for using our program.")