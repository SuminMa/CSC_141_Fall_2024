# 11-3. Employee - test_employee_with_a_fixture.py

import pytest
from employee import Employee

@pytest.fixture
def employee():
    """Provide a sample employee instance for testing."""
    return Employee('John', 'Doe', 50000)

def test_give_default_raise(employee):
    """Test that the default raise increases the salary by $5,000."""
    # Apply the default raise
    employee.give_raise()
    
    # Check if the salary is increased by $5,000
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    """Test that a custom raise amount works correctly."""
    # Apply a custom raise of $10,000
    employee.give_raise(10000)
    
    # Check if the salary is increased by $10,000
    assert employee.annual_salary == 60000