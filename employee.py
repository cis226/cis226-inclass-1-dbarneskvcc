class Employee:
    """Class to represent a single employee"""

    # Contants
    WEEKS_PER_YEAR = 52

    # 3 - 4 main parts to a class.

    # Constructor
    def __init__(self, first_name, last_name, weekly_salary):
        """Constructor"""

        # Attributes / Backing fields
        self.first_name = first_name
        self.last_name = last_name
        self.weekly_salary = weekly_salary

    # Methods
    def __str__(self):
        """String method"""
        # f"{self.first_name:<10} {self.last_name:<20} {self.weekly_salary:>14}"
        return (
            f"{self.first_name:<10}"
            f" {self.last_name:<20}"
            f" {self.weekly_salary:>14}"
        )

    def first_and_last_name(self):
        """Return first and last name concatenated together"""
        return f"{self.first_name:<10} {self.last_name:<20}"

    def apply_percentage_raise(self, percentage):
        """Accept a percentage raise and apply it to the salary"""
        self.weekly_salary = self.weekly_salary * (
            1 + (percentage / 100)
        )

    def _private_method(self):
        """Demo of a private method"""
        pass
        # This is just a demo of a private method.
        # methods that start with an _ should not be called
        # outside of the class they are defined in.

    # Maybe Properties?
    @property
    def formatted_yearly_salary(self):
        """Property for weekly salary formatted as currency"""
        return f"${(self.weekly_salary * self.WEEKS_PER_YEAR):.2f}"
