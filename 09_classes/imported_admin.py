# 9-11. Imported Admin
# Store the classes User, Privileges, and Admin in one module.
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

class Privileges:
    def __init__(self):
        # It stores a list of strings as described in Exercise 9-7.
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # Move the show_privileges() method to this class.
    def show_privileges(self):
        """Print a list of admin privilegese."""
        print(self.privileges)

# Make a Privileges instance as an attribute in the Admin class.
class Admin:
    def __init__(self):
        self.privileges = Privileges()