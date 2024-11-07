import pandas as pd
import Staff
from Patient import patients
class file_handler():
    
    staff_path = ""
    patients_path = ""
    
    def __init__(self,staff_path,patients_path):
        self.patients_path = patients_path
        self.staff_path = staff_path
    
    def getStaff(self):
        staff_file = pd.read_excel(staff_path)
        del staff_file[staff_file.columns[0]]
        staff_list = []
        for i in staff_file.keys():
            s = staff(i,i[0],i[1],i[2])
            staff_list.append(s)
            return staff_list
    
    def saveStaff(self,staff):
        pass
    
    def getPatients(self):
        patients_file = pd.read_excel(patients_path)
        del patients_file[patients_file.columns[0]]
        patients_list = []
        for i in patient_file.keys():
            s = patients(i,i[0],i[1],i[2])
            patients_list.append(s)
            return patients_list
    
    def savePatient(self,patient):
        pass
