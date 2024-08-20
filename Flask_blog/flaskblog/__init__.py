import os
from flask import Flask # import the flask app
from flask_sqlalchemy import SQLAlchemy # import the database
from flask_bcrypt import Bcrypt # import the bcrypt app
from flask_login import LoginManager # import the login manager
from flask_mail import Mail # import the mail app
from flaskblog.config import Config # import the config
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env file into environment
# create the flask app object
# configure database 
db = SQLAlchemy() # create the database
bcrypt = Bcrypt() # create the bcrypt app
login_manager = LoginManager() # create the login manager
login_manager.login_view = 'users.login' # set the login view
login_manager.login_message_category = 'info' # set the login message category


# create the mail app
Mail = Mail() # create the mail app

# create the app
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
# initialize the database, bcrypt, login manager, and mail app
    db.init_app(app) # initialize the database
    bcrypt.init_app(app) # initialize the bcrypt app
    login_manager.init_app(app) # initialize the login manager
    Mail.init_app(app) # initialize the mail app
# import the routes
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

# add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
    @app.after_request # add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response


    return app
