# 9-2. Three Restaurants
# Start with my class from Exercis 9-1.
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

# Create three different instances from the class
first_restaurant = Restaurant('Chichi', 'American')
second_restaurant = Restaurant('Mochi', 'Mexican')
third_restaurant = Restaurant('Hochi', 'Italian')

# Call describe_restaurant() for each instance.
first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()

