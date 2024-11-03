# 9-6. Ice Cream Stand
# An ice cream stand is a specific kind of restaurant.
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

# Write a class that inherits from the Restaurant class I wrote in Exercise 9-1.
class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to an ice cream stand."""
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(restaurant_name, cuisine_type)
        # Add an attribute called flavors that stores a list of ice cream flavors.
        self.flavors = ['mint chocolate', 'vanila', 'cookie and cream']

    # Write a method that displays these flavors.
    def display_flavor(self):
        """Print a statement displaying these flavors."""
        print(f"They have {self.flavors} flavors of ice cream.")

# Create an instance of IceCreamStand, and call display_flavor method.
IceCream = IceCreamStand('Kor', 'Korean')
IceCream.display_flavor()

