# 6-9. Favorite Places
# Think of three names to use as keys in the dictionary
'''
Emily
Erica
Monica
'''

# Make a dictionary called favorite_places
# Store one to three favorite places for each person
favorite_places = {
    'Emily': ['Paris', 'Denver', 'Chicago'],
    'Erica': ['New York', 'Philadelphia', 'California'],
    'Monica': ['Seoul', 'Tokyo', 'Jeju island']
}

# Loop through the dictionary, and print each person's name and their favorite places
for name, places in favorite_places.items():
    print(f"\n{name}'s favortie places are:")
    for place in places:
        print(f"\t{place}")