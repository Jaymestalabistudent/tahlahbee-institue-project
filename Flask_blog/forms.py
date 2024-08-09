from flask_wtf import FlaskForm # importing FlaskForm from flask_wtf
from wtforms import StringField, PasswordField, SubmitField, BooleanField # importing StringField, PasswordField, SubmitField, BooleanField from wtforms
from wtforms.validators import DataRequired, Length, Email, EqualTo # importing DataRequired, Length, Email, EqualTo from wtforms.validators


class RegistrationForm(FlaskForm): # creating a class called RegistrationForm by inheriting from FlaskForm
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=5, max=20)])  # creating a variable called username and assigning it to StringField this will validate the username
    email = StringField('Email',
                        validators=[DataRequired(), Email()]) # creating a variable called email and assigning it to StringField this will validate email
    password = PasswordField('Password', validators=[DataRequired()]) # creating a variable called password and assigning it to PasswordField this will validate password
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')]) # creating a variable called confirm_password and assigning it to PasswordField this will validate confirm_password if field is equal to the password field
    submit = SubmitField('Sign Up') # creating a variable called submit and assigning it to SubmitField this will validate the submit button

class LoginForm(FlaskForm): # creating a class called LoginForm by inheriting from FlaskForm
    email = StringField('Email',
                        validators=[DataRequired(), Email()]) # creating a variable called email and assigning it to StringField this will validate email
    password = PasswordField('Password', validators=[DataRequired()]) # creating a variable called password and assigning it to PasswordField this will validate password
    remember = BooleanField('Remember Me') # creating a variable called remember and assigning it to BooleanField this will validate the remember me checkbox
    submit = SubmitField('Login') # creating a variable called submit and assigning it to SubmitField this will validate the submit button
