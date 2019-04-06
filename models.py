import datetime
from peewee import *

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash



# Define db
DATABASE = SqliteDatabase('diggy.db')

#Since UserMixin is not the final class to be extended, it goes at beginning of inheritance chain
class User(UserMixin, Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True)
    password = CharField(max_length = 100)
    avatar = TextField()
    is_admin = BooleanField(default=False)
    #comes from backend - do not include in forms
    date_signed_in = DateTimeField(default= datetime.datetime.now)

    class Meta:
        database = DATABASE
        # order_by = ('-date_signed_in',) If not used, remove

    @classmethod
    def create_user(cls, first_name, last_name, email, password, avatar, admin=False):
        try:
            cls.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = generate_password_hash(password),
                avatar = avatar,
                is_admin = admin
                )
        except IntegrityError:
            raise ValueError("User/Email already exists") 



# Initialize connection to DATABASE
# Create table for User, 
# and close the connection
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()