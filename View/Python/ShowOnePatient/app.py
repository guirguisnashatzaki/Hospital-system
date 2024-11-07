from flask import Flask, render_template, request, redirect
from info import patientForm
import pandas as pd
from Model import Departement
from Model import Hospital
from Model import Patient
from Model import Person 
from Model import Staff
from Files import File_Handler
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

fh = file_handler('staff info data path','patient info data path')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/add-staff")
def add_staff():
    return render_template('add-staff.html', title='Add Staff')

@app.route("/add-patient")
def add_patient():
    form = patientForm()
    if request.method == 'GET' and (request.args):
        name = request.args['name']
        id = request.args['id']
        diseas = request.args['diseas']
        age = request.args['age']
        patient = Patient(name, id,diseas,age)
        fh.savePatient(patient)
    return render_template('add-patient.html', title='Add Patient', form =form)

@app.route("/show-staff")
def show_staff():
    return render_template('show-staff.html', title='Show Staff Data')

@app.route("/show-patient")
def show_patient():
    return render_template('show-patient.html', title='Show Patient Data')

@app.route("/show-one-staff")
def show_staff():
    return render_template('show-one-staff.html', title='Show one of Staff Data')

@app.route("/show-one-patient")
def show_patient():
    return render_template('show-one-patient.html', title='Show one of Patient Data')


if __name__ == '__main__':
    app.run(debug=True)

