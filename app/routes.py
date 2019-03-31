#View functions below map to one or more URLS so Flask knows what logic to implement when a client gives or goes to a given URL

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "What else can we display here! Now let the app devt BEGIN!"