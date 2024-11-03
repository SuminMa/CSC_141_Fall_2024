# 9-5. Login Attempts
# Add an attribute called login_attempts to your User class from Exercise 9-3.
class User:
    """A user profile."""
    def __init__(self, first_name, last_name, age, major):
        """Create attributes that are typically stored in a user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"Name: {self.first_name} {self.last_name}\nMajor: {self.major}\nAge: {self.age}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Nice to meet you.\n")

    # Write a method that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        """Show the number of login attempts."""
        self.login_attempts += 1
    
    # Write another method that resets the value of login_attempts to 0
    def reset_login_attempts(self):
        """Reset the value of login attempts."""
        self.login_attempts = 0

# Make an instance of the User class and call increment_login_attempts() several times.
user_01 = User('Sumin', 'Ma', '23', 'CS')

user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented properly.
print(user_01.login_attempts)

# Call reset_login_attempts().
user_01.reset_login_attempts()

# Print login_attempts again to make sure it was reset to 0.
print(user_01.login_attempts)


