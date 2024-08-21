import unittest
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# Define the forms as provided
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class ContributionForm(FlaskForm):
    content = TextAreaField('Your Contribution', validators=[DataRequired()])
    submit = SubmitField('Add to Story')

# Create a Flask application for testing
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF protection for testing

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

    def test_post_form_valid_data(self):
        form = PostForm(title="Sample Title", content="Sample Content")
        self.assertTrue(form.validate(), msg=f"Post form should be valid but got {form.errors}")

    def test_post_form_invalid_data(self):
        form = PostForm(title="", content="")
        self.assertFalse(form.validate(), msg=f"Post form should be invalid but got {form.errors}")

    def test_contribution_form_valid_data(self):
        form = ContributionForm(content="This is a contribution")
        self.assertTrue(form.validate(), msg=f"Contribution form should be valid but got {form.errors}")

    def test_contribution_form_invalid_data(self):
        form = ContributionForm(content="")
        self.assertFalse(form.validate(), msg=f"Contribution form should be invalid but got {form.errors}")

if __name__ == "__main__":
    unittest.main()
