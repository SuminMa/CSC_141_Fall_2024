# 11-3. Employee - employee.py

class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee with first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Give the employee a raise by adding to the annual salary."""
        self.annual_salary += amount
