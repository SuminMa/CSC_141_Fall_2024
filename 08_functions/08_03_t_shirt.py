# 8-3. T-Shirt

# Write a function called make_shirt() that accepts a size and the text of a msg.
def make_shirt(size, msg):
    # Print a sentence summarizing the size of the shirt and the message printed on it.
    print(f"Making a T-shirt in size {size} with '{msg}' printed on it.")

# Call the function once using positional arguments to make a shirt.
make_shirt('xs', 'Have a good day')

# Call the function a second time using keyword arguemnts.
make_shirt(size='xs', msg='Have a great day')
