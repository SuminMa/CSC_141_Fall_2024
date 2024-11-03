# 9-12. Multiple Modules
# Store the Admin class in one module
from multiple_modules_privileges import Privileges

class Admin:
    def __init__(self):
        self.privileges = Privileges()