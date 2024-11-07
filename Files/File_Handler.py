import pandas as pd
import Staff
import Patient 
class file_handler():
    
    staff_path = ""
    patients_path = ""
    
    def __init__(self,staff_path,patients_path):
        self.patients_path = patients_path
        self.staff_path = staff_path
    
    def getStaff(self):
        staff_file = pd.read_excel(self.staff_path)
        del staff_file[staff_file.columns[0]]
        staff_list = []
        for i in staff_file.keys():
            s = staff(i,i[0],i[1],i[2])
            staff_list.append(s)
        return staff_list
    
    def saveStaff(self,staff):
        staff_file[staff.name] = [staff.id, staff.diseas, staff.age]
        staff_file.to_excel(self.staff_path)
    
    def getPatients(self):
        patients_file = pd.read_excel(self.patients_path)
        del patients_file[patients_file.columns[0]]
        patients_list = []
        for i in patient_file.keys():
            s = Patient(i,i[0],i[1],i[2])
            patients_list.append(s)
        return patients_list
    
    def savePatient(self,patient):
        patient_file[patient.name] = [patient.id, patient.diseas, patient.age]
        patient_file.to_excel(self.patients_path)
