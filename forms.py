
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, FileField, IntegerField, HiddenField, SelectField, DateTimeField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email, Length, EqualTo)
from wtforms.fields.html5 import DateField
from models import User

# create the class and variables to house Field definitions
class UserForm(Form):
    first_name = TextField("First Name")
    last_name = TextField("Last Name")
    email = TextField("Email Address")
    role = TextField()
    avatar = StringField()
  



def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')

class SignupForm(Form):
    first_name = StringField(
        'First Name',
        validators=[
            DataRequired(),
            Length(min=2)
            ])
    last_name = StringField(
        'Last Name',
        validators=[
            DataRequired(),
            Length(min=2)
            ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
            ])        
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=3),
            EqualTo('password2', message='Passwords must match') 
            ])      
    password2 = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired()
            ])

class LoginForm(Form):
    email = StringField(
        'Email', 
        validators=[
            DataRequired(), 
            Email()
            ])
    password = PasswordField(
        'Password', 
        validators=[
            DataRequired()
            ])

class PatientDataForm(Form):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2)])
    gender = StringField('Gender')
    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    picture_upload = TextField('Patient photo')
    ssn = IntegerField('SSN', validators=[DataRequired()])
    health_insurance_id = IntegerField('Insurance ID', validators=[DataRequired()])
    address = StringField('Address')
    city = StringField('City')
    zip_code = IntegerField('Zip Code')
    phone_number = IntegerField('Phone Number')
    medical_history = TextAreaField('Medical History', validators=[DataRequired()])
    visit_notes = TextAreaField('Visit Notes', validators=[DataRequired()])
    dental_record = TextAreaField('Dental Record', validators=[DataRequired()])
    current_medication =  TextAreaField('Current Medication', validators=[DataRequired()])
    inactive_medication =  TextAreaField('Inactive Medication', validators=[DataRequired()])
    file_upload = TextField('Upload file')