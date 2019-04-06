import datetime
from peewee import *

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

import os

# Define db
DATABASE = SqliteDatabase('diggy')

class User(UserMixin, Model):
    first_name = TextField()
    last_name = TextField()
    email = CharField(unique=True)
    password = CharField(max_length = 100)
    role = TextField()
    avatar = TextField()
    #comes from backend - do not need in forms
    date_signed_in = DateTimeField(default= datetime.datetime.now)

    class Meta:
        database = DATABASE
        order_by = ('-date_signed_in',)

    @classmethod
    def create_user(cls, first_name, last_name, email, password, role, avatar):
        try:
            cls.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = generate_password_hash(password),
                role = role,
                avatar = avatar
                )
        except IntegrityError:
            raise ValueError("User/Email already exists") 



# Initialize connection to DATABASE
# Create table for User model, 
# and close the connection
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()