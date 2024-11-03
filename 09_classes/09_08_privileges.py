# 9-8. Privileges

# Write a separate Privileges class
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

# Create a new instance of Admin and use the method to show its privileges.
administrator = Admin()
administrator.privileges.show_privileges()