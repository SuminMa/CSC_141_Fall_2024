# 6-4. Glossary 2
# The previous glossary
glossary = {'traceback': 'a record of where the interpreter ran into trouble',
    'variables': 'labels that can be assigned to values',
    'string': 'a series of characters',
    'list': 'a collection of itmes in a particular order',
    'set': 'a collection in which each item must be unique'}

# Think of five more Python terms I've learned about in the previous chapters
'''
dictionary: a collection of key-value pairs
tuple: an immutable list
slice: a specific group of items
conditional test: an expression that can be evaluated as True or False
constant: a variable whose value stays the same throughout the life of a program
'''
# Assign them to a new dictionary
new_glossary = {'dictionary': 'a collection of key-value pairs',
    'tuple': 'an immutable list',
    'slice': 'a specific group of items',
    'conditional test': 'an expression that can be evaluated as True or False',
    'constant': 'a variable whose value stays the same throughout the life of a program'}
# Add new one to the previous glossary
glossary.update(new_glossary)

# When I run this program again, these new words and meanings shoud be
# automatically be included in the output
for word in glossary:
    print(f"The {word} means {glossary[word]}.")

