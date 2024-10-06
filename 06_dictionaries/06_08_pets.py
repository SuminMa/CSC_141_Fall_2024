# 6-8. Pets
# Make several dictionaries, where each dictionary represents a different pet
# In each dictionary, include the kind of animal and the owner's name
pet1 = {
    'name': 'love',
    'kind': 'dog',
    'owner': 'Charlotte'
    }

pet2 = {
    'name': 'joy',
    'kind': 'cat',
    'owner': 'Monica'
    }

pet3 = {
    'name': 'happy',
    'kind': 'tiger',
    'owner': 'Emily'
    }

pet4 = {
    'name': 'charlie',
    'kind': 'lion',
    'owner': 'Erica'
    }

# Store thease dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4]

# Loop through my list and as I do, print everything I know about each pet
for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']} whose owner is {pet['owner']}.")
