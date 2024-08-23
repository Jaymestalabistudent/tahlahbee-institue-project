import pytest
from flask import Flask, redirect, url_for, abort, request, render_template_string
from flask.testing import FlaskClient

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'

    @app.route('/post/new', methods=['GET', 'POST'])
    def new_post():
        if request.method == 'POST':
            return 'Post Created', 201
        return 'New Post Page'

    @app.route('/post/<int:post_id>')
    def view_post(post_id):
        return f'Post {post_id} Page'

    @app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
    def update_post(post_id):
        if request.method == 'POST':
            return f'Post {post_id} Updated', 200
        return f'Update Post {post_id} Page'

    @app.route('/post/<int:post_id>/delete', methods=['POST'])
    def delete_post(post_id):
        return 'Post Deleted'

    @app.route('/story-mode', methods=['GET', 'POST'])
    def story_mode():
        return 'Story Mode Page'

    @app.route('/story-mode/contribute', methods=['POST'])
    def contribute_to_story():
        return 'Contributed to Story'

    @app.route('/redirect-to-story')
    def redirect_to_story():
        return redirect(url_for('story_mode'))

    @app.route('/error')
    def error():
        abort(404)

    return app

@pytest.fixture
def client(app: FlaskClient):
    return app.test_client()

# Basic tests
def test_new_post(client):
    response = client.get('/post/new')
    assert response.data == b'New Post Page'
    assert response.status_code == 200

def test_view_post(client):
    response = client.get('/post/1')
    assert response.data == b'Post 1 Page'
    assert response.status_code == 200

def test_update_post(client):
    response = client.get('/post/1/update')
    assert response.data == b'Update Post 1 Page'
    assert response.status_code == 200

def test_delete_post(client):
    response = client.post('/post/1/delete')
    assert response.data == b'Post Deleted'
    assert response.status_code == 200

def test_story_mode(client):
    response = client.get('/story-mode')
    assert response.data == b'Story Mode Page'
    assert response.status_code == 200

def test_contribute_to_story(client):
    response = client.post('/story-mode/contribute')
    assert response.data == b'Contributed to Story'
    assert response.status_code == 200

# Additional tests
def test_form_submission(client):
    response = client.post('/post/new', data={'title': 'Test Post', 'content': 'Test Content'})
    assert response.data == b'Post Created'
    assert response.status_code == 201

def test_404_error(client):
    response = client.get('/this-route-does-not-exist')
    assert response.status_code == 404

def test_authentication_redirect(client):
    response = client.get('/redirect-to-story', follow_redirects=True)
    assert response.data == b'Story Mode Page'
    assert response.status_code == 200
