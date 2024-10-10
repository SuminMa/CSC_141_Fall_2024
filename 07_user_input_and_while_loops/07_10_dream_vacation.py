# 7-10. Dream Vacation
# Write a program that polls users about their dream vacation
# Write a prompt including a block of code that prints the result of the poll

dream_vacations = {}
# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    dream_vacation = input("If you could visit one place in the world, where would you go? ")
    
    # Store the response in the dictionary
    dream_vacations[name] = dream_vacation

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False      

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, dream_vacation in dream_vacations.items():
    print(f"{name} would like to go to {dream_vacation}.")