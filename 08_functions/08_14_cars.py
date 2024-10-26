# 8-14. Cars

# Write a function that stores information about a car in a dictionary.
# It should then accept an arbitrary number of keyword arguments.
def make_car(manu, model, **info):
    """stores information about a car in a dictionary."""
    # It should always receive a manufacturer and a model name.
    info['manufacturer'] = manu
    info['model'] = model
    return info

# Call the function with the required information and two other name-value pairs.
car = make_car('Telsa', 'Cyber Truck', color='silver', tow_package=True)

# Print the dictionary that's returned to make sure all the information was stored corretcly.
print(car)