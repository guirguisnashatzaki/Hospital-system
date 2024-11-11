import pandas as pd
from myModel.Staff import *
from myModel.Patient import *
class file_handler():
    
    staff_path = ""
    patients_path = ""
    
    def __init__(self,staff_path,patients_path):
        self.patients_path = patients_path
        self.staff_path = staff_path
    
    def getStaff(self):
        self.staff_file = pd.read_excel(self.staff_path)
        del self.staff_file[self.staff_file.columns[0]]
        staff_list = []
        for i in self.staff_file.keys():
            s = Staff(i,i[0],i[1],i[2])
            staff_list.append(s)
        return staff_list
    
    def saveStaff(self,staff):
        self.staff_file[staff.name] = [staff.id, staff.diseas, staff.age]
        self.staff_file.to_excel(self.staff_path)
    
    def getPatients(self):
        self.patients_file = pd.read_excel(self.patients_path)
        del self.patients_file[self.patients_file.columns[0]]
        patients_list = []
        for i in self.patients_file.keys():
            s = Patient(i,i[0],i[1],i[2])
            patients_list.append(s)
        return patients_list
    
    def savePatient(self,patient):
        self.patient_file[patient.name] = [patient.id, patient.diseas, patient.age]
        self.patient_file.to_excel(self.patients_path)
