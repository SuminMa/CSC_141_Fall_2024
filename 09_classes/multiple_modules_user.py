# 9-12. Multiple Modules
# Store the User class in one module
class User:
    """A user profile."""
    def __init__(self, first_name, last_name, age, major):
        """Create attributes that are typically stored in a user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"Name: {self.first_name} {self.last_name}\nMajor: {self.major}\nAge: {self.age}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Nice to meet you.\n")