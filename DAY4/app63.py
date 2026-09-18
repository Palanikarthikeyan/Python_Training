
class Enrollment:
    """Represents an employee enrollment record with basic identity details."""

    def __init__(self, name, dob, bloodgroup=""):
        """Initialize an employee record with required details.

        Args:
            name (str): Employee name.
            dob (str): Employee date of birth.
            bloodgroup (str, optional): Employee blood group. Defaults to empty string.
        """
        self.Name = name
        self.DOB = dob
        self.bloodgroup = bloodgroup

    def display_employee(self):
        """Print the employee details in a readable format."""
        print(f"Emp name is:{self.Name} DOB is:{self.DOB} BloodGroup is:{self.bloodgroup}")

    def __str__(self):
        """Return the employee record as a string."""
        return f"Emp name is:{self.Name} DOB is:{self.DOB} BloodGroup is:{self.bloodgroup}"


def display_employee_records(employees):
    """Display all employee records from a list of Enrollment objects.

    Args:
        employees (list[Enrollment]): List of employee objects.
    """
    for employee in employees:
        print(employee)


# Reusable object creation with required constructor arguments
obj1 = Enrollment("Arun", "1st Jan", "A+")
obj2 = Enrollment("Anu", "2nd Feb", "O+")

# Non-constructor display of employee records
employees = [obj1, obj2]
display_employee_records(employees)

# Individual display using method
obj1.display_employee()
obj2.display_employee()
print(str(obj1)) # obj1.__str__()