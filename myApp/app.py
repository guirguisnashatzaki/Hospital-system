from flask import Flask, render_template, request, redirect, url_for,flash
import FormClass.info as info
import pandas as pd
from File_Handler import *
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

fh = file_handler('Hospital-system\myApp\staff_data.xlsx','Hospital-system\myApp\patient_data.xlsx')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/add-staff', methods=['GET', 'POST'])
def staff_form():
    form = info.StaffForm()
    if form.validate_on_submit():
        Name = form.name.data
        Email = form.email.data
        Position = form.position.data
        Staff_ID = form.staff_id.data
        Hire_Date = form.hire_date.data.strftime('%Y-%m-%d')
        staff = Staff(Name, Hire_Date, Position, Staff_ID, Email)
        fh.saveStaff(staff)
        flash('Patient data saved successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add-staff.html', form=form)

@app.route("/add-patient", methods=['GET', 'POST'])
def add_patient():
    form = info.patientForm()
    if form.validate_on_submit():
        name = form.name.data
        patient_id = form.patient_id.data
        issues = form.issues.data
        age = form.age.data
        email = form.email.data
        appointment_date = form.appointment_date.data
        type_of_medicine = form.type_of_medicine.data
        patient = Patient(name, patient_id,issues,age,email,appointment_date,type_of_medicine)
        fh.savePatient(patient)
        flash('Patient data saved successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add-patient.html', title='Add Patient', form =form)

@app.route("/show-staff")
def show_staff():
    all_staff = fh.getStaff()
    
    return render_template('show-staff.html', title='Show Staff Data',all_staff=all_staff)

@app.route("/show-patient", methods=['GET', 'POST'])
def show_patient():
    all_patient = fh.getPatients()
    return render_template('show-patient.html', title='Show Patient Data',all_patient =all_patient)

'''@app.route("/show-one-staff")
def show_staff():
    return render_template('show-one-staff.html', title='Show one of Staff Data')
'''
if __name__ == '__main__':
    app.run(debug=True)

