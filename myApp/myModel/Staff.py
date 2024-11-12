from . import myperson

class Staff(myperson.Person):
    position = ""
    """Class for hospital staff, inheriting from Person."""
    def __init__(self, name, age, position, staff_id,email):
        super().__init__(name, age)
        self.position = position
        self.staff_id = staff_id
        self.email = email
        
    def view_info(self):
        """View staff information."""
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"