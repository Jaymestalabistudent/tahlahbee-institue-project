from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


# create posts
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