import os 
from dotenv import load_dotenv

class Config: 
    """
    Class to store configuration variables. Each configuration setting a weeks class variable.
    """
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY') 
    