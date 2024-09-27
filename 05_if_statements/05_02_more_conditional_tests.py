#5-2. More Conditional Tests
#Have at least one True and one False result for each of the following

#Tests for eqality and inequality with strings
sweets = 'Chocolate'
#True
print("\nIs sweets == 'Chocolate'? I predict True")
print(sweets == 'Chocolate')
#False
print("\nIs sweets == 'Candy'? I predict False")
print(sweets == 'Candy')

#Tests using the lower() method
#True
print("\nIs sweets.lower() == 'chocolate'? I predict True")
print(sweets.lower() == 'chocolate')
#False
print("\nIs sweets.lower() == 'Chocolate'? I predict False")
print(sweets.lower() == 'Chocolate')

#Numerical tests involving equality and inequality, greater than and less than,
#greater than or equal to, and less than or equal to
year = 2024
#Equality
#True
print("\nIs year == 2024? I predict True")
print(year == 2024)
#False
print("\nIs year == 2023? I predict False")
print(year == 2023)

#Inequality
#True
print("\nIs year != 2023? I predict True")
print(year != 2023)
#False
print("\nIs year != 2024? I predict False")
print(year != 2024)

#Greater than and less than
#True
print("\nIs (year > 2000) and (year < 3000)? I predict True")
print((year > 2000) and (year < 3000))
#False
print("\nIs (year > 1000) and (year < 1500)? I predict False")
print((year > 1000) and (year < 1500))

#Greater than or equal to, and less than or equal to
#True
print("\nIs (year >= 2000) and (year <= 3000)? I predict True")
print((year >= 2000) and (year <= 3000))
#False
print("\nIs (year >= 1000) and (year <= 1500)? I predict False")
print((year >= 1000) and (year <= 1500))

#Tests using the and keyword and the or keyword
#True
print("\nIs (year >= 2) and (year <= 3) or (year == 2024)? I predict True")
print((year >= 2) and (year <= 3) or (year == 2024))
#False
print("\nIs (year >= 2) and (year <= 3) or (year == 24)? I predict False")
print((year >= 2) and (year <= 3) or (year == 24))

#Test whether an item is in a list
fruits = ['apple', 'pear', 'lemon']
#True
print("\nIs 'apple' in fruits? I predict True")
print('apple' in fruits)
#False
print("\nIs 'strawberry' in fruits? I predict False")
print('strawberry' in fruits)

#Test whether an item is not in a list
#True
print("\nIs 'strawberry' not in fruits? I predict True")
print('strawberry' not in fruits)
#False
print("\nIs 'apple' not in fruits? I predict False")
print('apple' not in fruits)
