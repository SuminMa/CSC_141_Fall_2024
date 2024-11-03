# 9-10. Imported Restaurant
# Using your latest Restaurant class, store it in a module.

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