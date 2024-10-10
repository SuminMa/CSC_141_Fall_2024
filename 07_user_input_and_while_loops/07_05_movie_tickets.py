# 7-5 Movie Tickets
# A movie theater charges different ticket prices depending on a person's age

# Write a loop in which I ask users their age, and then tell them the cost
while True:
    age = int(input("How old are you? "))
# If a person is under the age of 3, the ticket is free
    if age < 3:
        print("The ticket for you is free.")
# If they are between 3 and 12, the ticket is $10
    elif age > 3 and age < 12:
        print("The ticket for you would be $10.")
# If they are over age 12. the ticket is $15
    else:
        print("The ticket for you would be $15.")