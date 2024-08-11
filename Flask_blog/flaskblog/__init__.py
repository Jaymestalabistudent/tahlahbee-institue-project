from flask import Flask     # import the flask module
from flask_sqlalchemy import SQLAlchemy     # import the sqlalchemy module
from flask_bcrypt import Bcrypt     # import the bcrypt module
from flask_login import LoginManager     # import the login manager module

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

# import the routes
from flaskblog import routes

# add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
@app.after_request # add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
