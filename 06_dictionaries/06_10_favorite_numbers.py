# 6-10. Favorite Numbers
# Modify my program from Exercise 6-2 so each person can have more than one favorite number
fav_num = {
    'RM': ['5', '1'],
    'Emily': ['7', '17'],
    'Xavier': ['44', '22'],
    'Edgar': ['7', '3'],
    'Erica': ['11', '4']
    }

# Print each person's name along with their favorite numbers
for name, numbers in fav_num.items():
    print(f"\n{name}'s favortie numbers are:")
    for number in numbers:
        print(f"\t{number}")