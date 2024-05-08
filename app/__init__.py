from flask import Flask

# Create an instance of Flask to use as our application object
#  __name__ indicates this module is our starting point for resource loading
app = Flask(__name__)

# From our app package, import the routes module 
from app import routes

