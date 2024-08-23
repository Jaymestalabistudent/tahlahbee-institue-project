# Testing Tutorial
## Dependencies

To set up testing for a Flask application, you need the following dependencies:

1. **Flask**: The web framework.
2. **Flask-WTF**: For form handling.
3. **Flask-Testing**: For testing Flask applications.
4. **pytest**: For running tests.
5. **unittest**: Python's built-in testing framework.
6. **pytest-mock**: For mocking in pytest.
7. **Flask-Login**: For user session management.

You can install these dependencies using pip:

```sh
pip install Flask Flask-WTF Flask-Testing pytest pytest-mock Flask-Login
```

### Plan

1. Create a new Markdown file named `TESTING_TUTORIAL.md`.
2. Add sections for dependencies, setting up the Flask application for testing, writing tests, and running the tests.
3. Include code snippets and explanations for each section.

### Code

```markdown
# Testing Tutorial

## Dependencies

To set up testing for a Flask application, you need the following dependencies:

1. **Flask**: The web framework.
2. **Flask-WTF**: For form handling.
3. **Flask-Testing**: For testing Flask applications.
4. **pytest**: For running tests.
5. **unittest**: Python's built-in testing framework.
6. **pytest-mock**: For mocking in pytest.
7. **Flask-Login**: For user session management.

You can install these dependencies using pip:

```sh
pip install Flask Flask-WTF Flask-Testing pytest pytest-mock Flask-Login
```

## Setting Up the Flask Application for Testing

1. **Create a Test Configuration**: Disable CSRF protection and use an in-memory SQLite database for testing.

```python
class TestConfig:
    SECRET_KEY = 'mysecret'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
```

2. **Create the Flask Application**: Define a factory function to create the app with the test configuration.

```python
from flask import Flask

def create_app(config_class=TestConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Initialize extensions like SQLAlchemy, LoginManager, etc.
    return app
```

## Writing Tests

### Form Tests

Validate form data using `Flask-WTF` forms.

```python
import unittest
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo

class SimpleRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class BasicFormTestCase(unittest.TestCase):
    def test_registration_form_valid_data(self):
        form = SimpleRegistrationForm(username="validuser", email="valid@example.com", password="password", confirm_password="password")
        self.assertTrue(form.validate())

    def test_registration_form_invalid_username(self):
        form = SimpleRegistrationForm(username="", email="valid@example.com", password="password", confirm_password="password")
        self.assertFalse(form.validate())
```

### Route Tests

Test route access and redirection.

```python
import pytest
from flask import Flask
from flaskblog import create_app, db
from flaskblog.models import User

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_user(app):
    user = User(username='testuser', email='test@example.com', password='password')
    db.session.add(user)
    db.session.commit()
    return user

def test_home_redirect_anonymous(client):
    response = client.get('/')
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'].startswith('/login')
```

### Error Handler Tests

Ensure custom error pages are returned.

```python
import unittest
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def error_404(error):
        return "404 Not Found", 404

    @app.errorhandler(500)
    def error_500(error):
        return "500 Internal Server Error", 500

    return app

class ErrorHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_404_error(self):
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"404 Not Found", response.data)

    def test_500_error(self):
        response = self.client.get('/cause-error')
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"500 Internal Server Error", response.data)
```

### Model Tests

Test model creation and interactions.

```python
import unittest
from unittest.mock import patch, MagicMock
from flaskblog import create_app
from flaskblog.models import User, Post, Story, Contribution

class BasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def test_post_creation(self):
        with patch('flaskblog.models.Post.query') as mock_query:
            mock_post = MagicMock()
            mock_post.title = 'Test Post'
            mock_post.content = 'This is a test post'
            mock_query.first.return_value = mock_post
            post = Post(title='Test Post', content='This is a test post', user_id=1)
            self.assertEqual(post.title, 'Test Post')
            self.assertEqual(post.content, 'This is a test post')
```

## Running the Tests

To run the tests, you can use `pytest` or `unittest`.

```sh
pytest
```

or

```sh
python -m unittest discover
```

This setup ensures that your Flask application is thoroughly tested, covering forms, routes, error handlers, and models.

# Run the tests using pytest get html report
pip install pytest-html pytest --upgrade --force-reinstall
```sh
pytest
```

$ pytest --html=report.html --self-contained-html

# Output: flaskblog/docs/test_results/report.html

