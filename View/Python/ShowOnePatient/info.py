from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from openpyxl import load_workbook
class patientForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=2, max=20)])
    id = IntegerField('Id', validators=[DataRequired()])
    diseas = StringField('Diseas',validators=[DataRequired()])
    age = IntegerField('Age ',validators=[DataRequired()])
    submit = SubmitField('save')
