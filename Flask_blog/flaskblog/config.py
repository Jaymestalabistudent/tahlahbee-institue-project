import os
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env file into environment

# configure database # TODO: change to postgresql
class Config :
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key') # temp secret key for the app
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')
# sqlite database this will be temp until move over to postgresql'
    # configure the mail server
    MAIL_SERVER = 'smtp.gmail.com' # set the mail server
    MAIL_PORT = 587 # set the mail port
    MAIL_USE_TLS = True # set the mail use tls
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # Company email address
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') # Company email password

