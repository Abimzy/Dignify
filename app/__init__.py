#FLASK APPLICATION INSTANCE

# Create app object as an instance of class Flask imported from flask package

from flask import Flask

app = Flask(__name__)

#routes modules below script is to avoid circular imports so it only references the app variable in this script
from app import routes

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)


