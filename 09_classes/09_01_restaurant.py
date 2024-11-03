# 9-1. Restaurant
# Make a class called Restaurant
class Restaurant:
    """Simple information about a restaurant."""
    # The __init__() method for Restaurant should store two attributes.
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints these two pieces of information."""
        print(f"{self.restaurant_name} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints a messages indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is open.")

# Make an instance called restaurant from my class
restaurant = Restaurant('Kor', 'Korean')

# Print the two attributes individually and then call both methods.
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

