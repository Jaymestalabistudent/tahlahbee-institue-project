import os
from dotenv import load_dotenv
load_dotenv()  # variables from .env file configure your own locally

# database
class Config :
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # configure the mail server
    MAIL_SERVER = 'smtp.gmail.com' # set the mail server
    MAIL_PORT = 587 # set the mail port
    MAIL_USE_TLS = True # set the mail use tls
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # Company email address
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') # Company email password

