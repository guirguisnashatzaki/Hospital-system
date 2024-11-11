class Hospital:
    name = ""
    location = ""
    departements = []
    """Class for managing hospital operations."""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []  # List to hold departments

    def add_department(self, department):
        """Add a department to the hospital."""
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")