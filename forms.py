
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, FileField, IntegerField, HiddenField, SelectField

# import User model
from models import User

# create the class and variables to house Field definitions
class UserForm(Form):
    id = IntegerField()
    first_name = TextField("First Name")
    last_name = TextField("Last Name")
    email = TextField("Email Address")
    role = TextField()
    avatar = StringField()
    submit = SubmitField("Update")
