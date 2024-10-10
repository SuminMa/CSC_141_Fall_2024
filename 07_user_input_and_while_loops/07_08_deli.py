# 7-8. Deli
# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['toamto', 'avocado', 'egg', 'tuna', 'ham']

# Make an empty list called finished_sandwiches
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    # Loop through the list of sandwich orders and print a message for each order
    print(f"I made your {sandwich} sandwich.")
    # As each sandwich is made, move it to the list of finished sandwiches
    finished_sandwiches.append(sandwich)
    
# After all the sandwiches have been made, print a message listing each one tha was made
for sandwich in finished_sandwiches:
    print(f"\nThe {sandwich} was made.")

