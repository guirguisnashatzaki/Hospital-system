import Person

class Patient(Person):
    medical_record = ""
    """Class for hospital patients, inheriting from Person."""
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        """View patient record."""
        return f"Patient Record: {self.medical_record}"