# 9-7. Admin
# An administrator is a special kind of user.

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

# Write a class called Admin that inherits from the User class you wrote in Exerecise 9-3.
class Admin(User):
    def __init__(self, first_name, last_name, age, major):
        super().__init__(first_name, last_name, age, major)
        # Add an attribute, privileges, that stores a list of admin privileges.
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # Write a method that lists the administrator’s set of privileges.
    def show_privileges(self):
        """Print a list of admin privilegese."""
        print(self.privileges)

# Create an instance of Admin, and call show_privileges.
administrator = Admin('Sumin', 'Ma', '23', 'Computer Science')
administrator.show_privileges()
