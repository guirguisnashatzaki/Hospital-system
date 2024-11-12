from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class StaffForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    position = StringField('Position', validators=[DataRequired(), Length(max=30)])
    staff_id = IntegerField('Staff ID', validators=[DataRequired(), NumberRange(min=1)])
    hire_date = DateField('Hire Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    patient_id = IntegerField('Patient ID', validators=[DataRequired(), NumberRange(min=1)])
    appointment_date = DateField('Appointment Date', format='%Y-%m-%d', validators=[DataRequired()])
    type_of_medicine = TextAreaField('Type of Medicine', validators=[DataRequired(), Length(max=200)])
    issues = TextAreaField('Issues', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Submit')
