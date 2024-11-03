# 9-4. Number Served
# Start with my program from Exercise 9-1.
class Restaurant:
    """Simple information about a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
         # Add an attribute called number_served with a default value of 0.
        self.number_served = 0

    def describe_restaurant(self):
        """Prints these two pieces of information."""
        print(f"{self.restaurant_name} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints a messages indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is open.")

    # Add a method that sets the number of customers that have been served.
    def set_number_served(self, number):
        """Print a statement showing the number served."""
        self.number_served = number

    # Add a method that increments the number of customers who've been served.
    def increment_number_served(self, amount):
        """Add the given amount to the number served."""
        self.number_served += amount

# Create an instance called restaurant from this class.
restaurant = Restaurant('Kor', 'Korean')

# Print the number of customers the restaurant has served.
print(restaurant.number_served)
# Change that value and print it again.
restaurant.number_served = 3
print(restaurant.number_served)

# Call set_number_served() with a new number and print the value again.
restaurant.set_number_served(10)
print(restaurant.number_served)

# Call increment_number_served() with any number
restaurant.increment_number_served(5)
print(restaurant.number_served)