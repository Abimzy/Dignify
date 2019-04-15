from flask import Flask, g
from flask import render_template, flash, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
import datetime 
import secrets
import os


from forms import UserForm, UpdateAccountForm

#To have access to models
import models
import forms



app = Flask(__name__)
app.secret_key = 'uyghbfedivjnfecsvohldfnsjhln'

# LoginManager sets up our session for app
login_manager = LoginManager()
login_manager.init_app(app)
#sets up default login view 
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

   
# Handle requests when they come in (before) and when they complete (after)
@app.before_request
def before_request():
    """Connect to the DB before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user
 
@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    #'form' variable sent to profile template defined here
    form = forms.UserForm()
    # checks if form submission is valid
    if form.validate_on_submit():
        # if it is, create the User's profile 
        models.User.create(
            first_name=form.first_name.data.strip(), 
            last_name=form.last_name.data.strip(), 
            email=form.email.data.strip(),
            bio=form.bio.data.strip(),
            avatar=form.avatar.data.strip()
            ) 
   
    # Add bio section here! use ckeditor plugin
        flash("Your profile has been updated", "alert alert-success")
        return redirect ('charts') 
    return render_template('profile.html', title="Profile", form=form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.SignupForm()
    if form.validate_on_submit():
        models.User.create_user(
            first_name = form.first_name.data.strip(), 
            last_name = form.last_name.data.strip(), 
            email = form.email.data.strip(), 
            bio=form.bio.data.strip(),
            password = form.password.data.strip()
            )
        flash('Your account has been created', "alert alert-success")
        return redirect(url_for('login')) #return on successful POST request
    return render_template('signup.html', form=form) #return on successful GET request
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    ## handle the post request
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match", "alert alert-danger")
        else:
            if check_password_hash(user.password, form.password.data):
                ## login our user/create session
                login_user(user)

                return redirect(url_for('charts'))

            else:
                flash("Your email or password doesn't match", "alert alert-danger")
 
    ### get request
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out", "alert alert-success")
    return redirect(url_for('home'))



#User account page
@app.route('/account')
@login_required
def account():
    avatar = url_for('static', filename='profile_pics/' + current_user.avatar)

    flash('Your account has been updated', "alert alert-success")

    return render_template('account.html', title="Account", avatar=avatar)


#Save profile picture
def save_picture(avatar_pic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(avatar_pic.filename)
    avatar_fn = random_hex + f_ext
    avatar_path = os.path.join(app.root_path, 'static/profile_pics', avatar_fn)
    avatar_pic.save(avatar_path)

    return avatar_fn



#User account update
@app.route('/update_account/<id>', methods=['GET', 'POST'])
@login_required
def update_account(id):
    user_param = int(id)
    user = models.User.get(models.User.id == user_param)
    avatar = url_for('static', filename='profile_pics/' + current_user.avatar)

    form = forms.UpdateAccountForm()
    if form.validate_on_submit():
        if form.avatar.data:
            picture_file = save_picture(form.avatar.data)
            user.avatar = picture_file
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.email = form.email.data
            user.bio = form.bio.data
                
            user.save()
        flash('Your account has been updated', "alert alert-success")
        return redirect(url_for('account'))

    return render_template('update_account.html', title="Account", avatar=avatar, form=form, user=user)






@app.route('/patient_form', methods=['GET', 'POST'])
@login_required
def patient_form():
    form = forms.PatientDataForm()

    if form.validate_on_submit():
        models.PatientData.create(
            user = g.user._get_current_object(),
            first_name = form.first_name.data.strip(),
            last_name = form.last_name.data.strip(),
            gender = form.gender.data.strip(),
            date_of_birth = form.date_of_birth.data,
            picture_upload = form.picture_upload.data.strip(),
            ssn = form.ssn.data,
            health_insurance_id = form.health_insurance_id.data,
            address = form.address.data.strip(),
            city = form.city.data,
            zip_code = form.zip_code.data,
            phone_number = form.phone_number.data,
            medical_history = form.medical_history.data.strip(),
            visit_notes = form.visit_notes.data.strip(),
            dental_record = form.dental_record.data.strip(),
            current_medication = form.current_medication.data.strip(),
            inactive_medication = form.inactive_medication.data.strip(),
            file_upload = form.file_upload.data.strip() 
            )
       
        flash('Your profile is updated', "alert alert-success")
        return redirect(url_for('charts')) 
    return render_template('patient_form.html', form=form, chart=chart)

# Rendering all patient records as cards(limit to 100/pg) on charts route
@app.route('/charts')
@login_required
def charts():
    patient_list = models.PatientData.select().limit(100)
    return render_template('charts.html', patient_list=patient_list)

#Rendering patient record by id
@app.route('/chart/<id>/', methods=['GET', 'POST'])
@login_required
def chart(id):
    chart = models.PatientData.get( models.PatientData.id == id)
    return render_template('chart.html' , chart=chart )



#Edit PatientData
@app.route('/edit_patient_data/<id>', methods=['GET', 'POST'])
@login_required
def edit_patient_data(id):
    chart = models.PatientData.get( models.PatientData.id == id)

    form = forms.PatientDataForm()
    if form.validate_on_submit():
        chart.first_name = form.first_name.data
        chart.last_name = form.last_name.data
        chart.gender = form.gender.data
        chart.date_of_birth = form.date_of_birth.data
        chart.picture_upload = form.picture_upload.data
        chart.ssn = form.ssn.data
        chart.health_insurance_id = form.health_insurance_id.data
        chart.address = form.address.data
        chart.city = form.city.data
        chart.zip_code = form.zip_code.data
        chart.phone_number = form.phone_number.data
        chart.medical_history = form.medical_history.data
        chart.visit_notes = form.visit_notes.data
        chart.dental_record = form.dental_record.data
        chart.current_medication = form.current_medication.data
        chart.inactive_medication = form.inactive_medication.data
        chart.file_upload = form.file_upload.data

        chart.save()

        flash('Patient chart is updated', "alert alert-success")
        return redirect(url_for('charts'))

    return render_template('edit_patient_data.html' , chart=chart, form=form) 
     

#Delete PatientData
@app.route('/delete_patient_data/<id>', methods=['GET', 'DELETE'])
@login_required
def delete_patient_data(id):
    chart = models.PatientData.get( models.PatientData.id == id)

    chart.delete_instance()

    flash('Patient chart deleted', "alert alert-warning")
    return redirect(url_for('charts'))





if __name__ == '__main__':
# before app runs, we initialize a connection to the models
    models.initialize()

    # Sample admin profile here to initialize model
    try:
        models.User.create_user(
            first_name = 'Jane',
            last_name = 'Doe',
            email = 'jane@email.com',
            password = 'password',
            bio='About me',
            admin = True
            )
    except ValueError:
        pass 

    app.run(debug=True) 