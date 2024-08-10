from datetime import datetime, timezone
from flaskblog import db




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # default image for user profile will uploaded later
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # lazy loading to get all the post of the user in one query relationship between the post and the user

    def __repr__(self):
        return f"User('{self.username}', '{self.email}'), {self.image_file}" # this is how the object is printed out


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc)) # default  time zone
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # foreign key to the user table this is the link between the files so that the post and the user are connected
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')" # this is how the object is printed out
