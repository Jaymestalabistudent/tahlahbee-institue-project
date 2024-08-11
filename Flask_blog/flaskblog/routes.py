from flask import render_template, url_for, flash, redirect, request # import the render template, url for, flash, redirect and request
from flaskblog import app, db, bcrypt   # import the app, db and bcrypt from the flaskblog package
from flaskblog.forms import RegistrationForm, LoginForm # import the registration form and login form
from flaskblog.models import User, Post # import the user model and post model
from flask_login import login_user, current_user, logout_user, login_required # import the login user, current user, logout user and login required


# create a list of dictionaries to store the post data test data
posts = [
    {
        'author': 'tahlahbee institute',
        'title': 'first Post 1',
        'content': 'First post content',
        'date_posted': 'August 12, 2024'
    },
    {
        'author': 'tahlahbee broadcast',
        'title': 'second Post 2',
        'content': 'Second post content',
        'date_posted': 'August 11, 2024'
        },
    {
        'author': 'hood news',
        'title': 'third Post 2',
        'content': 'Second post content',
        'date_posted': 'August 01, 2024'
    }
]

# create a route for pages
@app.route("/") # create a route for the home page
@app.route("/home") # create a route for the home page
@login_required # create a route for the home page
def home(): # create a route for the home page
    return render_template('home.html', posts=posts) # create a route for the home page


@app.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')

# create a route for the register page
@app.route("/register", methods=['GET', 'POST']) # create a route for the register page
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home')) # create a route for the register page
    form = RegistrationForm() # create a route for the register page
    if form.validate_on_submit(): # create a route for the register page
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # create a route for the register page
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # create a route for the register page
        db.session.add(user) # create a route for the register page
        db.session.commit() # create a route for the register page
        flash('Your account has been created! You are now able to log in', 'success') # create a route for the register page
        return redirect(url_for('login')) # create a route for the register page
    return render_template('register.html', title='Register', form=form) # create a route for the register page

# create a route for the login page
@app.route("/login", methods=['GET', 'POST']) # create a route for the login page
def login():
    if current_user.is_authenticated: # create a route for the login page
        return redirect(url_for('home')) # create a route for the login page
    form = LoginForm() # create a route for the login page
    if form.validate_on_submit(): # create a route for the login page
        user = User.query.filter_by(email=form.email.data).first()  # create a route for the login page
        if user and bcrypt.check_password_hash(user.password, form.password.data): # create a route for the login page
            login_user(user, remember=form.remember.data)    # create a route for the login page
            next_page = request.args.get('next')  # create a route for the login page
            return redirect(next_page) if next_page else redirect(url_for('login')) # create a route for the login page
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger') # create a route for the login page
    return render_template('login.html', title='Login', form=form)

# create a route for the logout and accounts pages
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login')) # redirect to the login page and add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login check __init__.py


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

# create a route for the post page
@app.route("/post")
@login_required
def post():
    return render_template('post.html')

# additional routes
@app.route("/tahlahbee")
def tahlahbee():
    return render_template('tahlahbee.html', title = 'test page')

@app.route("/info")
@login_required
def info():
    return render_template('info.html', title = 'Information')

@app.route("/spotify")
@login_required
def spotify():
    return render_template('spotify.html', title = 'Music and Podcast')

@app.route("/video")
@login_required
def video():
    return render_template('video.html', title = 'Movies and Series')

@app.route("/events")
@login_required
def events():
    return render_template('events.html', title = 'Meet with us')