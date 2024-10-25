# 8-4. Large Shirts

# Modify the make_shirt() function.
# Shirts are large by default with a message that reads I love Python.
def make_shirt(size='large', msg='I love Python'):
    # Print a sentence summarizing the size of the shirt and the message printed on it.
    print(f"Making a T-shirt in size {size} with '{msg}' printed on it.")
    
# Make a large shirt and a medium shirt with the default message.
make_shirt() # a large shirt
make_shirt(size='medium') # a medium shirt

# Make a shirt of any size with a different message.
make_shirt(size='small', msg='We love you')