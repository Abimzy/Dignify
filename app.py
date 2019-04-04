from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home', )



@app.route('/landing')
def landing():
    return render_template('landing.html', title="Home" )


if __name__ == '__main__':
    app.run(debug=True)