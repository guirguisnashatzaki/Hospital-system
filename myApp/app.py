from flask import Flask, render_template, request, redirect, url_for
import FormClass.info as info
import pandas as pd
from File_Handler import *
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

@app.route('/add-staff', methods=['GET', 'POST'])
def staff_form():
    form = info.StaffForm()
    if form.validate_on_submit():
        data = {
            'Name': form.name.data,
            'Email': form.email.data,
            'Position': form.position.data,
            'Staff ID': form.staff_id.data,
            'Hire Date': form.hire_date.data.strftime('%Y-%m-%d')
        }
        #save_data('staff_data.csv', data, headers=['Name', 'Email', 'Position', 'Staff ID', 'Hire Date'])
        #flash('Staff data saved successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add-staff.html', form=form)

@app.route("/add-patient")
def add_patient():
    form = info.patientForm()
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

'''@app.route("/show-one-staff")
def show_staff():
    return render_template('show-one-staff.html', title='Show one of Staff Data')
'''
if __name__ == '__main__':
    app.run(debug=True)

