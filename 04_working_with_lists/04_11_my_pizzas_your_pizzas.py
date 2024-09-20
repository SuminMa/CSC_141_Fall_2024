#4-11. My Pizzas, Your Pizzas

#start with my program from Exercise 4-1
pizzas = ['pineapple', 'cheese', 'meat']

#make a copy of the list of pizzas and call it friend_pizzas
friend_pizzas = pizzas[:]

#add a new pizza to the original list
pizzas.append('potato')

#add a different pizza to to the list friend_pizzas
friend_pizzas.append('sweet potato')

#print the message My favorite pizzas are:
print("My favorite pizzas are:")

#use a for loop to print the first list
for pizza in pizzas:
    print(pizza)

#print the message My friend's favortie pizzas are:
print("\nMy friend's favortie pizzas are:")

#use a for loop to print the second list
for pizza in friend_pizzas:
    print(pizza)