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


class PatientData(Model):
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    date_of_birth = DateTimeField(default=datetime.datetime)
    picture_upload = TextField()
    SSN = IntegerField(unique=True)
    health_insurance_id = IntegerField(unique=True)
    address = CharField()
    city = CharField()
    zip_code = IntegerField()
    phone_number = IntegerField()
    medical_history = CharField()
    visit_notes = CharField()
    dental_record = CharField()
    current_medication =  CharField()
    inactive_medication =  CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    file_upload = TextField()
    user = ForeignKeyField(
        model=User,
        backref='patient_data'
    )


    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


# Initialize connection to DATABASE
# Create table for User, 
# and close the connection
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, PatientData], safe=True)
    DATABASE.close()