# Import Flask Library
from flask import Flask, render_template

# Create a flask app using the flask object
app = Flask(__name__)

# Define URLs e.g:
#      @app.route('www.yourdomain.com/')
#      Passing a variable through URL 
#      @app.route('/home/urs/<string:name>/posts/<int:id>')
#      def hello(name, id):
#          return "Hello world! " + name + ", your id is: " + str(id)
#
#      
#
#      find the closest function to run:

@app.route('/')
def index():
    return render_template('index.html') # will find the files under "templates" folder

@app.route('/postOnly', methods=['POST'])
def post_req():
    return "You can only use post method"

# Enable debug mode when running on cmd. 
if __name__ == "__main__":
    app.run(debug=True)