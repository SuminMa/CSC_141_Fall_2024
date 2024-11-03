# 9-12. Multiple Modules
# Store the Privileges class in one module
class Privileges:
    def __init__(self):
        # It stores a list of strings as described in Exercise 9-7.
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # Move the show_privileges() method to this class.
    def show_privileges(self):
        """Print a list of admin privilegese."""
        print(self.privileges)