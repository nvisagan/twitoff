<<<<<<< HEAD
#import flask package. flask makes app objects.
from flask import Flask, render_template

#create Flask web server, makes the application
=======
#To run:FLASK_APP=hello.py 
#flask run
#import flask package. flask makes app objects

from flask import Flask, render_template

#Create Flask web server, makes the application 
>>>>>>> 733c7619e86ae4507085ce1528b23828919aa5b7
app = Flask(__name__)

#routes determine location
@app.route("/")

#Define simple function
def home():
    return render_template('home.html')

@app.route("/about")
def preds():
    return render_template('about.html')
<<<<<<< HEAD
=======

>>>>>>> 733c7619e86ae4507085ce1528b23828919aa5b7
