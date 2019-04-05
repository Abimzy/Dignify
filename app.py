from flask import Flask, g
from flask import render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = 'uyghbfedivjnfecsvohldfnsjhln'
   

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home" )


if __name__ == '__main__':
    app.run(debug=True)