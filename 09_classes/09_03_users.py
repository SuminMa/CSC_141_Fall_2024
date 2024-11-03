# 9-3. Users
# Make a class called User
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

# Create several instances representing different users.
user_01 = User('Erin', 'Hu', '22', 'Nursing')
user_02 = User('Zinn', 'Kim', '23', 'Music')
user_03 = User('Hannah', 'Swift', '20', 'Art')

# Call both methods for each user.
user_01.describe_user()
user_01.greet_user()
user_02.describe_user()
user_02.greet_user()
user_03.describe_user()
user_03.greet_user()
