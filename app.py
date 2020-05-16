# Import Flask Library
from flask import Flask


# Create a flask app using the flask object
app = Flask(__name__)


# Define URLs e.g:
#      @app.route('www.yourdomain.com/')
#      find the closest function to run:
@app.route('/')
@app.route('/home')
def hello():
    return "Hello world!"


# Enable debug mode when running on cmd. 
if __name__ == "__main__":
    app.run(debug=True)