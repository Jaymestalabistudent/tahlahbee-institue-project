import os
from flask import Flask # import the flask app
from flask_sqlalchemy import SQLAlchemy # import the database
from flask_bcrypt import Bcrypt # import the bcrypt app
from flask_login import LoginManager # import the login manager
from flask_mail import Mail # import the mail app
# create the flask app object
app = Flask(__name__)

# configure the app
# TODO: Change secret key before deploying
app.config['SECRET_KEY'] = 'a46f003cee2a82c1db483b145bb45717' # temp secret key for the app

# configure database # TODO: change to postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # sqlite database this will be temp until move over to postgresql'
db = SQLAlchemy(app) # create the database
bcrypt = Bcrypt(app) # create the bcrypt app
login_manager = LoginManager(app) # create the login manager
login_manager.login_view = 'login' # set the login view
login_manager.login_message_category = 'info' # set the login message category

# configure the mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # set the mail server
app.config['MAIL_PORT'] = 587 # set the mail port
app.config['MAIL_USE_TLS'] = True # set the mail use tls
app.config['MAIL_USERNAME'] = 'tahlahbee.institute@gmail.com' # Company email address
app.config['MAIL_PASSWORD'] = 'frog hkko rsow vtox' # Company email password

# create the mail app
Mail = Mail(app) # create the mail app

# import the routes
from flaskblog import routes

# add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
@app.after_request # add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
