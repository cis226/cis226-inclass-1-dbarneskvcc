"""Program code"""

from employee import Employee

def main(*args):
    """Method to run program"""

    # Make a new instance of the Employee class.
    my_employee = Employee("David", "Barnes", 1234.56)

    print(my_employee)

    # Can change attributes on the instance if needed
    my_employee.first_name = "New first name"
    my_employee.last_name = "New-Last"
    my_employee.weekly_salary = 23456.98
    print(my_employee)

    my_sec_employee = Employee("Employee", "Deux", 45.67)

    print(my_sec_employee)

    my_sec_employee.apply_percentage_raise(50)
    print(my_sec_employee)
    print(my_sec_employee.formatted_yearly_salary)

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
    print(employees)
