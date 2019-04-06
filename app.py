from flask import Flask, g
from flask import render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap

from forms import UserForm

#To have access to models
import models



app = Flask(__name__)
app.secret_key = 'uyghbfedivjnfecsvohldfnsjhln'

   
# Handle requests when they come in (before) and when they complete (after)
@app.before_request
def before_request():
    """Connect to the DB before each request."""
    g.db = models.DATABASE
    g.db.connect()

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
    form = UserForm()
    # checks if the form submission is valid
    if form.validate_on_submit():
        # if it is, we update the User's profile 
        models.User.create(
            first_name=form.first_name.data.strip(), 
            last_name=form.last_name.data.strip(), 
            email=form.email.data.strip(),
            # role=form.role.data.strip(), How to swap this as admin option 
            avatar=form.avatar.data.strip()
            ) 
        flash("Your profile has been updated")
        return redirect ('/')
    return render_template('profile.html', title="Profile", form=form)


if __name__ == '__main__':
# before app runs, we initialize a connection to the models
    models.initialize()

    #Sample admin profile here
    try:
        models.User.create_user(
            first_name = 'Jane',
            last_name = 'Doe',
            email = 'jane@email.com',
            password = 'password',
            avatar = 'avatar',
            admin = True
            )
    except ValueError:
        pass

    app.run(debug=True) 