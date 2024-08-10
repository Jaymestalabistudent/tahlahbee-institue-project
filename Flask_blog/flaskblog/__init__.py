from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create flask app object
app = Flask(__name__)

# TODO: Change secret key before deploying
app.config['SECRET_KEY'] = 'a46f003cee2a82c1db483b145bb45717' # temp secret key for the app

# configure database # TODO: change to postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # sqlite database this will be temp until move over to postgresql
# initialize database
db = SQLAlchemy(app)


# import routes from the routes
from flaskblog import routes