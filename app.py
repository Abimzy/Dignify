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

@app.route('/profile')
def profile():
    #'form' variable sent to profile template defined here
    form = UserForm()
    return render_template('profile.html', title="Profile", form=form)


if __name__ == '__main__':
# before app runs, we initialize a connection to the models
    models.initialize()
    app.run(debug=True) 