"""Program code"""
# System Imports
import os
# First-Party Imports
from employee import Employee
from user_interface import UserInterface

def main(*args):
    """Method to run program"""

    # Make a new instance of the Employee class.
    # my_employee = Employee("David", "Barnes", 1234.56)

    # print(my_employee)

    # Can change attributes on the instance if needed
    # my_employee.first_name = "New first name"
    # my_employee.last_name = "New-Last"
    # my_employee.weekly_salary = 23456.98
    # print(my_employee)

    # my_sec_employee = Employee("Employee", "Deux", 45.67)
    # The following won't work because the method is private
    # my_sec_employee.__private_method()

    # print(my_sec_employee)

    # my_sec_employee.apply_percentage_raise(50)
    # print(my_sec_employee)
    # print(my_sec_employee.formatted_yearly_salary)


    # Make a new instance of the UserInterface class
    ui = UserInterface()

    # Instances of classes can be stored in a list.
    # Just like any other type in python
    employees = []
    employees.append(
        Employee("David", "Barnes", 835.00)
    )
    employees.append(
        Employee("James", "Kirk", 453.00)
    )
    employees.append(
        Employee("Jean-Luc", "Picard", 290.00)
    )

    # Get some input from the user
    selection = ui.display_menu_and_get_response()

    # While the choice they selected is not 2, continue to do work.
    while selection != ui.MAX_MENU_CHOICES:
        # See if the input they sent is equal to 1.
        if selection == 1:
            # Create string for concatination
            output_string = ""

            # Convert each employee to a string and add it to the
            # outputstring
            for employee in employees:
                # Concatenate to the output_string
                output_string += f"{employee}{os.linesep}"

            # Use the UI class to print out the string
            ui.print_list(output_string)

        # Check for different choice here, if there were more.

        # Lastly, re-prompt user for input on what to do.
        selection = ui.display_menu_and_get_response()

