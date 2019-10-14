""" Main application for twitoff"""

#imports
from flask import Flask

def create_app():
    """create and configures an instance of a flask app"""
    app = Flask(__name__)
    
    @app.route('/')
    def root():
        return "Welcome to our app"
    return app