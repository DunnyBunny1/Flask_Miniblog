from flask import Flask
from config import Config

# Create an instance of Flask to use as our application object
#  __name__ indicates this module is our starting point for resource loading
app = Flask(__name__)

# Read and apply the configuration file to this flask instance
app.config.from_object(Config)

# From our app package, import the routes module
from app import routes