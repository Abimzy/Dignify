
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, FileField, IntegerField, HiddenField, SelectField, DateTimeField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email, Length, EqualTo)

from models import User

# create the class and variables to house Field definitions
class UserForm(Form):
    first_name = TextField("First Name")
    last_name = TextField("Last Name")
    email = TextField("Email Address")
    role = TextField()
    avatar = StringField()
    submit = SubmitField("Update")



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
    avatar = StringField(
        'Picture (optional)'
        )
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