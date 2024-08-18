from datetime import datetime # This is used to get the current date and time
from itsdangerous import URLSafeTimedSerializer as Serializer
from flaskblog import db, login_manager, app # This is used to create the database
from flask_login import UserMixin # This is used to create the login manager

# load the user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# create the user class
class User(db.Model, UserMixin): # create the user class
    id = db.Column(db.Integer, primary_key=True) # create the user id
    username = db.Column(db.String(20), unique=True, nullable=False) # create the username
    email = db.Column(db.String(120), unique=True, nullable=False) # create the email
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # create the image file
    password = db.Column(db.String(60), nullable=False) # create the password
    posts = db.relationship('Post', backref='author', lazy=True) # create the posts
    contributions = db.relationship('Contribution', backref='author', lazy=True) # create the contributions

# create the reset token
    def get_reset_token(self, expires_sec=1800): # get the reset token
        s = Serializer(app.config['SECRET_KEY'], expires_sec) # create the serializer
        return s.dumps({'user_id': self.id}).decode('utf-8') # return the token


# verify the reset token
    @staticmethod # verify the reset token
    def verify_reset_token(token): # verify the reset token
        s = Serializer(app.config['SECRET_KEY']) # create the serializer
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# create the post class
class Post(db.Model): # create the post class
    id = db.Column(db.Integer, primary_key=True) # create the post id
    title = db.Column(db.String(100), nullable=False) # create the post title
    date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now) # create the post date
    content = db.Column(db.Text, nullable=False) # create the post content
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # create the user id

# create the post representation
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')" # return the post title and date

# create the story class
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True) # create the story id
    title = db.Column(db.String(100), nullable=False) # create the story title
    description = db.Column(db.Text, nullable=False) # create the story description
    contributions = db.relationship('Contribution', backref='story', lazy=True) # create the contributions

# create the contribution class
class Contribution(db.Model): # create the contribution class
    id = db.Column(db.Integer, primary_key=True) # create the contribution id
    content = db.Column(db.Text, nullable=False) # create the contribution content
    date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now) # create the contribution date
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False) # create the story id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # create the user id

