import pytest
from flask import Flask
from flaskblog import create_app, db
from flaskblog.models import User
from flask_login import login_user

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
    assert response.status_code == 302  # 302 is the HTTP status code for redirection
    assert 'Location' in response.headers
    assert response.headers['Location'].startswith('/login')

def test_info_redirect_anonymous(client):
    response = client.get('/info')
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'].startswith('/login')

def test_home_authenticated(client, auth_user):
    with client.session_transaction() as session:
        session['_user_id'] = auth_user.id
    response = client.get('/')
    assert response.status_code == 200

def test_info_authenticated(client, auth_user):
    with client.session_transaction() as session:
        session['_user_id'] = auth_user.id
    response = client.get('/info')
    assert response.status_code == 200
