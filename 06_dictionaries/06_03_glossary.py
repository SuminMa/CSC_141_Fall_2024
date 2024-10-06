# 6-3. Glossary
# Think of five programming words I've learned about in the previous chapters.
'''
traceback: a record of where the interpreter ran into trouble
variables: labels that can be assigned to values
string: a series of characters
list: a collection of itmes in a particular order
set: a collection in which each item must be unique
'''

# Use these words as the keys in my glossary, and store their meanings as values.
glossary = {'traceback': 'a record of where the interpreter ran into trouble',
    'variables': 'labels that can be assigned to values',
    'string': 'a series of characters',
    'list': 'a collection of itmes in a particular order',
    'set': 'a collection in which each item must be unique'}

# Print each word and its meaning as neatly formatted output.
for word in glossary:
    print(f"The {word} means {glossary[word]}.")