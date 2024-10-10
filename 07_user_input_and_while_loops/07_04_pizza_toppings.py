# 7-4. Pizza Toppings
# Write a loop that prompts the user to enter a series of pizza toppings
prompt = "\nWhat toppings would you like to add to your pizza?"
prompt += "\n(Enter 'quit' when you are finished.): "
toppings = ""
while toppings != 'quit': # The program stops when they enter a 'quit' value
    toppings = input(prompt)

    if toppings == 'quit':
        print(f"\nYour order has been placed. Thank you.")
        break
    else: #As they enter each topping, print a mmsage saying I'll add that topping
        print(f"I'll add {toppings} to your pizza!")