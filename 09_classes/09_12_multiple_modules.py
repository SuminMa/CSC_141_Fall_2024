# 9-12. Multiple Modules
"""Store the User class in one module, and store the
Privileges and Admin classes in a separate module."""
from multiple_modules_admin import Admin

# Create an Admin instance.
admin = Admin()

# Call show_privileges() to show that everything is still working correctly.
admin.privileges.show_privileges()