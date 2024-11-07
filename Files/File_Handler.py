import pandas as pd
class file_handler():
    
    staff_path = ""
    patients_path = ""
    
    def __init__(self,staff_path,patients_path):
        self.patients_path = patients_path
        self.staff_path = staff_path
    
    def getStaff(self):
        patient_file = pd.read_excel('patient.xlsx')
        del patient_file[patient_file.columns[0]]
        
    
    def saveStaff(self,staff):
        pass
    
    def getPatients(self):
        pass
    
    def savePatient(self,patient):
        pass
