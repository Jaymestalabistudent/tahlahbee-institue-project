from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime, timezone


# create flask app object
app = Flask(__name__)

# TODO: Change secret key before deploying
app.config['SECRET_KEY'] = 'a46f003cee2a82c1db483b145bb45717' # temp secret key for the app

# configure database # TODO: change to postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # sqlite database this will be temp until move over to postgresql
# initialize database
db = SQLAlchemy(app)

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

posts = [
    {
        'author': 'Tahlahbee Institute',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 08, 2024'
    },
    {
        'author': 'Institute',
        'title': 'Blog Post 2',
        'content': 'New post content',
        'date_posted': 'August 09, 2024'
    },
    {
       'author': 'tahlahbee institute',
        'title': 'Blog Post 3',
        'content': 'New post content',
        'date_posted': 'August 10, 2024'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


@app.route("/layout")
def layout():
    return render_template('layout.html', title = 'layout')


@app.route("/login", methods=['GET', 'POST']) # methods to allow the form to accept post request in browser
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@tahlahbee.com' and form.password.data == 'institute': # check if the email and password is correct
            flash('Welcome in!', 'success')
            return redirect(url_for('home'))  # redirect to home page when login is success full using the function in the flaskblog.py
        else:
            flash(f'Nope Unsuccessful. Please check username and password', 'danger') # flash message to send a one time alert to the user using form.username.data to get the username and success is the bootstrap class success
    return render_template('login.html', title='Login', form=form)

@app.route("/register" , methods = ['GET', 'POST']) # methods to allow the form to accept post request in browser
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success') # flash message to send a one time alert to the user using form.username.data to get the username and success is the bootstrap class success
        return redirect(url_for('home')) # redirect to home page when login is success full using the function in the flaskblog.py
    return render_template('register.html',  title = 'Register Please', form = form)

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/tahlahbee")
def tahlahbee():
    return render_template('tahlahbee.html', title = 'test page')

@app.route("/info")
def info():
    return render_template('info.html', title = 'Information')

@app.route("/spotify")
def spotify():
    return render_template('spotify.html', title = 'Music and Podcast')

@app.route("/video")
def video():
    return render_template('video.html', title = 'Movies and Series')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)  # Run the Flask development server
