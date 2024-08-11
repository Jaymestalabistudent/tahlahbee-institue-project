from flask_wtf import FlaskForm # import the flask form class
from wtforms import StringField, PasswordField, SubmitField, BooleanField   # import the string field, password field, submit field and boolean field
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError    # import the data required, length, email, equal to and validation error
from flaskblog.models import User # import the user model from the models.py file

# define the registration form
class RegistrationForm(FlaskForm):  # create a class called registration form that inherits from the flask form class
    username = StringField('Username',  # create a string field called username
                        validators=[DataRequired(), Length(min=2, max=20)]) # set the validators for the username field
    email = StringField('Email',
                        validators=[DataRequired(), Email()]) # set the validators for the email field
    password = PasswordField('Password', validators=[DataRequired()]) # set the validators for the password field
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')]) # set the validators for the confirm password field
    submit = SubmitField('Sign Up') # set the validators for the submit field


# validate the username and email fields in  the login form
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Nope that username is taken. Please choose a different one.') # check if the username is already taken

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Mmm that email is taken. Please choose a different one.') # check if the email is already taken

# define the login form
class LoginForm(FlaskForm): # create a class called login form that inherits from the flask form class
    email = StringField('Email',
                        validators=[DataRequired(), Email()]) # set the validators for the email field
    password = PasswordField('Password', validators=[DataRequired()]) # set the validators for the password field
    remember = BooleanField('Remember Me') # set the validators for the remember me field
    submit = SubmitField('Login') # set the validators for the submit field
