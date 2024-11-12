import pandas as pd
from myModel.Staff import *
from myModel.Patient import *
class file_handler():
    
    def __init__(self,staff_path,patients_path):
        self.patients_path = patients_path
        self.staff_path = staff_path
        self.staff_file = pd.read_excel(self.staff_path)
        self.patient_file = pd.read_excel(self.patients_path)
        if self.staff_file.empty == False :
            del self.staff_file[self.staff_file.columns[0]]
        if self.patient_file.empty == False :
            del self.patient_file[self.patient_file.columns[0]]
    
    def getStaff(self):
 
        staff_list = []
        for i in self.staff_file.keys():
            s = Staff(i,self.staff_file[i][2],self.staff_file[i][0],self.staff_file[i][1],self.staff_file[i][3])
            
            staff_list.append(s)
        return staff_list
    
    def saveStaff(self,staff):
        self.staff_file[staff.name] = [staff.position, staff.staff_id, staff.age, staff.email]
        self.staff_file.to_excel(self.staff_path)
    
    def getPatients(self):
        
        patients_list = []
        for i in self.patient_file.keys():
            s = Patient(i,self.patient_file[i][0],self.patient_file[i][1],self.patient_file[i][2],self.patient_file[i][3],self.patient_file[i][4],self.patient_file[i][5])
            patients_list.append(s)
        return patients_list
    
    def savePatient(self,patient):
        self.patient_file[patient.name] = [patient.patient_id, patient.issues, patient.age,patient.email,patient.appointment_date,patient.type_of_medicine]
        self.patient_file.to_excel(self.patients_path)
        
