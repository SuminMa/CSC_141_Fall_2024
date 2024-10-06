# 6-6. Polling
# Use the code in favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }
# Make a list of people who should take the favorite languages poll
# Include some names that are already in the dictionary and some that are not
people = ['jen', 'sarah', 'edward', 'phil', 'rose', 'jennie', 'risa']

# Loop through the list of people who should take the poll
for person in people:
    # If they have already taken the poll, print a message thanking them for responding
    if person in favorite_languages.keys():
        print(f"Thank you for responding, {person}!")
    # If they have not taken the poll, print a message inviting them to take the poll
    else:
         print(f"I'd like to invite you to take the poll, {person}.")