import unittest
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo

# Setup Flask application for testing
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF protection for testing

class SimpleRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class SimpleLoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SimpleRequestResetForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class SimpleResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class BasicFormTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the application context."""
        cls.app = app
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        """Pop the application context."""
        cls.app_context.pop()

    def setUp(self):
        """Setup the test environment before each test."""
        pass

    def tearDown(self):
        """Clean up after each test."""
        pass

    def test_registration_form_valid_data(self):
        form = SimpleRegistrationForm(username="validuser", email="valid@example.com", password="password", confirm_password="password")
        self.assertTrue(form.validate(), msg=f"Registration form should be valid but got {form.errors}")

    def test_registration_form_invalid_username(self):
        form = SimpleRegistrationForm(username="", email="valid@example.com", password="password", confirm_password="password")
        self.assertFalse(form.validate(), msg=f"Registration form should be invalid but got {form.errors}")

    def test_registration_form_invalid_email(self):
        form = SimpleRegistrationForm(username="validuser", email="invalidemail", password="password", confirm_password="password")
        self.assertFalse(form.validate(), msg=f"Registration form should be invalid but got {form.errors}")

    def test_login_form_valid_data(self):
        form = SimpleLoginForm(email="valid@example.com", password="password")
        self.assertTrue(form.validate(), msg=f"Login form should be valid but got {form.errors}")

    def test_login_form_invalid_email(self):
        form = SimpleLoginForm(email="invalidemail", password="password")
        self.assertFalse(form.validate(), msg=f"Login form should be invalid but got {form.errors}")

    def test_request_reset_form_valid_email(self):
        form = SimpleRequestResetForm(email="valid@example.com")
        self.assertTrue(form.validate(), msg=f"Request reset form should be valid but got {form.errors}")

    def test_request_reset_form_invalid_email(self):
        form = SimpleRequestResetForm(email="invalidemail")
        self.assertFalse(form.validate(), msg=f"Request reset form should be invalid but got {form.errors}")

    def test_reset_password_form_valid_data(self):
        form = SimpleResetPasswordForm(password="newpassword", confirm_password="newpassword")
        self.assertTrue(form.validate(), msg=f"Reset password form should be valid but got {form.errors}")

    def test_reset_password_form_invalid_data(self):
        form = SimpleResetPasswordForm(password="newpassword", confirm_password="mismatch")
        self.assertFalse(form.validate(), msg=f"Reset password form should be invalid but got {form.errors}")

if __name__ == "__main__":
    unittest.main()
