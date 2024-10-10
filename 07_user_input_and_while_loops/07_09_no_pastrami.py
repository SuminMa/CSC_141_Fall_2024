# 7-9 No Pastrami
# Using the list sandwich_orders from Excercies 7-8
# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['toamto', 'avocado', 'egg', 'tuna', 'ham']

# Make sure the sandwich 'pastrami' appears in the list at least three times
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
print()
print(sandwich_orders)

# Print a message saying the deli has run out of pastrami
print("\nPastrami has run out of order.")

# Use a while loop to remove all occurrences of 'pastrami' from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make sure no pastrami sandwiches end up in the list
print()
print(sandwich_orders)