from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, DateField,TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from openpyxl import load_workbook
class patientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    age = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    patient_id = IntegerField('Patient ID', validators=[DataRequired(), NumberRange(min=1)])
    appointment_date = DateField('Appointment Date', format='%Y-%m-%d', validators=[DataRequired()])
    type_of_medicine = TextAreaField('Type of Medicine', validators=[DataRequired(), Length(max=200)])
    issues = TextAreaField('Issues', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Submit')
# Form for Staff
class StaffForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    position = StringField('Position', validators=[DataRequired()])
    staff_id = IntegerField('Staff ID', validators=[DataRequired()])
    hire_date = DateField('Hire Date', validators=[DataRequired()])
    submit = SubmitField('Submit')