from datetime import datetime # This is the datetime module from the Python standard library
from itsdangerous import URLSafeTimedSerializer as Serializer # This is the URLSafeTimedSerializer module from the itsdangerous library in Flask
from flaskblog import db, login_manager, app # This is the db, login_manager, and app modules from the flaskblog package
from flask_login import UserMixin # This is the UserMixin module from the flask_login package

# This is the load_user function from the login_manager module
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# This is the User class that inherits from the db.Model and UserMixin classes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)  # Add the username column
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')  # Add the image_file column
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # Add the posts relationship
    contributions = db.relationship('Contribution', backref='author', lazy=True)  # Add the contributions relationship

# This is the get_reset_token function that generates a reset token for the user
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], salt='reset-salt')  # No need for .decode('utf-8')
        return s.dumps({'user_id': self.id}, salt='reset-salt')  # No need for .decode('utf-8')
# This is the verify_reset_token function that verifies the reset token for the user
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'], salt='reset-salt')  # No need for .decode('utf-8')
        try:
            user_id = s.loads(token, salt='reset-salt')['user_id']  # No need for .decode('utf-8')
        except Exception as e:
            print(f"Error verifying token: {e}")
            return None
        return User.query.get(user_id)  # No need for .decode('utf-8') or int() or .encode('utf-8')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# This is the Post class that inherits from the db.Model class
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# This is the __repr__ function that returns the title and date of the post
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# This is the Story class that inherits from the db.Model class
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    contributions = db.relationship('Contribution', backref='story', lazy=True)

    def __repr__(self):
        return f"Story('{self.title}')"

# This is the Contribution class that inherits from the db.Model class
class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# This is the __repr__ function that returns the content and date of the contribution
    def __repr__(self):
        return f"Contribution('{self.content}', '{self.date_posted}')"
