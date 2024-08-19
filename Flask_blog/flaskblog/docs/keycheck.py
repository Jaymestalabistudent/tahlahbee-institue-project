import os # import the os module to interact with the operating system
from flask import Flask
from flask import current_app # import the current application

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a46f003cee2a82c1db483b145bb45717' # temp secret key for the app

# Print information about SECRET_KEY
with app.app_context():
    print(f'SECRET_KEY: {current_app.config["SECRET_KEY"]}')
    print(f'Type of SECRET_KEY: {type(current_app.config["SECRET_KEY"])}')
    print(f'SECRET_KEY (encoded): {current_app.config["SECRET_KEY"].encode("utf-8")}')
    print(f'Type after encoding: {type(current_app.config["SECRET_KEY"].encode("utf-8"))}')
