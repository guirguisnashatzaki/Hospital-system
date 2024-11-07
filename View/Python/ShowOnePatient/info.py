from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from openpyxl import load_workbook
class patientForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    id = PasswordField('Id', validators=[DataRequired()])
    age = PasswordField('Age ',
                                     validators=[DataRequired()])
    submit = SubmitField('save')
