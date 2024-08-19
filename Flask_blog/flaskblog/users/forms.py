from flask_wtf import FlaskForm  # import the flask form
from flask_wtf.file import FileField, FileAllowed, FileRequired # import the file field
from flask_login import current_user # import the current user
from wtforms import StringField, PasswordField, SubmitField, BooleanField # import the string field, password field, submit field and booleanfield textarea field
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError # import the validators
from flaskblog.models import User # import the user model

# create a registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)]) # create a username field
    email = StringField('Email',
                        validators=[DataRequired(), Email()])    # create an email field
    password = PasswordField('Password', validators=[DataRequired()]) # create a password field
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')]) # create a confirm password field
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() # check if the username already exists
        if user:
            raise ValidationError('That username is taken. Please choose a different one.') # if the username already exists, raise an error

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() # check if the email already exists
        if user:
            raise ValidationError('That email is taken. Please choose a different one.') # if the email already exists, raise an error

# create a login form
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()]) # create an email field
    password = PasswordField('Password', validators=[DataRequired()]) # create a password field
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# create a update account form form
class UpdateAccountForm(FlaskForm): # create an update account form
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)]) # create a username field
    email = StringField('Email',
                        validators=[DataRequired(), Email()])    # create an email field
    picture = FileField('Profile picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'])]) # create a picture field
    submit = SubmitField('Update') # create a submit field

    def validate_username(self, username): # validate the username
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first() # check if the username already exists
            if user:
                raise ValidationError('That username is taken. Please choose a different one.') # if the username already exists, raise an error

    def validate_email(self, email): # validate the email
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()    # check if the email already exists
            if user:
                raise ValidationError('That email is taken. Please choose a different one.') # if the email already exists, raise an error

# create a request reset form
class RequestResetForm(FlaskForm): # create a request reset form
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset') # create a submit field

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Request Sent. Please check your email. or try again later.')

# create a reset password form
class ResetPasswordForm(FlaskForm): # create a reset password form
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password') # create a submit field