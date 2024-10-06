# 6-7. People
# Start with the program I wrote for Excercise 6-1
friend = {
    'first_name': 'Emily',
    'last_name': 'Ma',
    'age': '22',
    'city': 'Dallas'
    }

# Make two new dictionaries representing different people
new_friend_1 = {
    'first_name': 'Sojin',
    'last_name': 'Kim',
    'age': '24',
    'city': 'Seoul'
    }
new_friend_2 = {
    'first_name': 'Drew',
    'last_name': 'Kim',
    'age': '23',
    'city': 'New York'
    } 
# Store all three dictionaries in a list called people
people = []
people.append(friend)
people.append(new_friend_1)
people.append(new_friend_2)

# Loop through my list of people, printing everything I know about each person
for friend in people:
    first_name = friend['first_name']
    last_name = friend['last_name']
    age = friend['age']
    city = friend['city']
    
    print(f"My friend {first_name} {last_name} is {age} years old and lives in {city}.")