from . import myperson

class Patient(myperson.Person):
    issues = ""
    
    """Class for hospital patients, inheriting from Person."""
    def __init__(self, name, age, issues,patient_id,email,appointment_date,type_of_medicine):
        super().__init__(name, age)
        self.issues = issues
        self.patient_id = patient_id
        self.email = email
        self.appointment_date = appointment_date
        self.type_of_medicine = type_of_medicine
    def view_record(self):
        """View patient record."""
        return f"Patient Record: {self.medical_record}"