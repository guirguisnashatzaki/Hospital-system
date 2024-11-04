from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, IntegerField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
import csv
import os
from faker import Faker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
fake = Faker()

# Form for Patient
class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    medical_issue = TextAreaField('Medical Issue', validators=[DataRequired(), Length(max=200)])
    medicine_type = SelectField('Type of Medicine', choices=[('Tablet', 'Tablet'), ('Syrup', 'Syrup'), ('Injection', 'Injection')], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for Staff
class StaffForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    position = StringField('Position', validators=[DataRequired()])
    staff_id = IntegerField('Staff ID', validators=[DataRequired()])
    hire_date = DateField('Hire Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

def save_data(filename, data, headers):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/patient', methods=['GET', 'POST'])
def patient_form():
    form = PatientForm()
    if form.validate_on_submit():
        data = {
            'Name': form.name.data,
            'Email': form.email.data,
            'Date of Birth': form.date_of_birth.data.strftime('%Y-%m-%d'),
            'Medical Issue': form.medical_issue.data,
            'Medicine Type': form.medicine_type.data
        }
        save_data('patient_data.csv', data, headers=['Name', 'Email', 'Date of Birth', 'Medical Issue', 'Medicine Type'])
        flash('Patient data saved successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('patient_form.html', form=form)

@app.route('/staff', methods=['GET', 'POST'])
def staff_form():
    form = StaffForm()
    if form.validate_on_submit():
        data = {
            'Name': form.name.data,
            'Email': form.email.data,
            'Position': form.position.data,
            'Staff ID': form.staff_id.data,
            'Hire Date': form.hire_date.data.strftime('%Y-%m-%d')
        }
        save_data('staff_data.csv', data, headers=['Name', 'Email', 'Position', 'Staff ID', 'Hire Date'])
        flash('Staff data saved successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('staff_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
