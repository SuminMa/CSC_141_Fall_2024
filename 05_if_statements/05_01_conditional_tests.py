#5-1. Conditional Tests
'''
Write a series of conditional tests
Print a statement describing each test and your prediction for the results
Create at least 10 tests
Have at least 5 tests evaluate to True and another 5 tets evaluate to False
'''

car = 'subaru'
#Checking for Equality
#1(True)
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
#2(False)
print("\nIs car == 'audi'? I predict False.")
print(car == ' audi')
#Ingoring Case When Checking for Equality
#3(True)
print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')
#4(False)
#Two values with different capitalization are not considered equal
print("\nIs car.lower() == 'Subaru'? I predict False.")
print(car.lower() == 'Subaru')
#Checking for Inequality
#5(True)
print("\nIs car != 'bmw'? I predict True.")
print(car != 'bmw')
#6(False)
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')
#Checking Multiple Conditions
#7(True)
print("\nIs car != 'bmw' and car != 'audi'? I predict True.")
print(car != 'bmw' and car != 'audi')
#8(False)
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')
#Checking Whether a Value Is in a List
#9(True)
cars = ['audi', 'subaru', 'bmw', 'benz']
print("\nIs car in cars? I predict True.")
print(car in cars)
#10(False)
print("\nIs car not in cars? I predict False.")
print(car not in cars)
