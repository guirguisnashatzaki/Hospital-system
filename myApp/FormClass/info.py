from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, EmailField, DateField
from wtforms.validators import DataRequired, Length, Email
from openpyxl import load_workbook
class patientForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=2, max=20)])
    id = IntegerField('Id', validators=[DataRequired()])
    diseas = StringField('Diseas',validators=[DataRequired()])
    age = IntegerField('Age ',validators=[DataRequired()])
    submit = SubmitField('save')
# Form for Staff
class StaffForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    position = StringField('Position', validators=[DataRequired()])
    staff_id = IntegerField('Staff ID', validators=[DataRequired()])
    hire_date = DateField('Hire Date', validators=[DataRequired()])
    submit = SubmitField('Submit')