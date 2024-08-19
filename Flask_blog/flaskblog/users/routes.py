from flask import render_template, url_for, flash, redirect, request, Blueprint, current_app # import the render_template, url_for, flash, redirect, request modules
from flask_login import login_user, current_user, logout_user, login_required # import the login_user, current_user, logout_user, and login_required modules
from flaskblog import db, bcrypt, Mail # import the  db, bcrypt and  mail modules
from flaskblog.models import User, Post
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from flaskblog.users.utils import save_picture
from flask_mail import Message # import the Message module from the flask_mail module

users = Blueprint('users', __name__) # create a blueprint for the users

# create a route for the register page
@users.route("/register", methods=['GET', 'POST']) # create a route for the register page
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home')) # redirect to the home page if the user is already authenticated
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # generate a hashed password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # pass the username, email, and hashed password to the User model
        db.session.add(user) # db session add the user
        db.session.commit() # commit the db session
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form) #  render the register page

# create a route for the login page
@users.route("/login", methods=['GET', 'POST']) # create a route for the login page
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # check the password hash
            login_user(user, remember=form.remember.data) # login the user
            next_page = request.args.get('next')   # get the next page
            return redirect(next_page) if next_page else redirect(url_for('users.login')) #  redirect to the next page if it exists
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger') # flash a login unsuccessful message
    return render_template('login.html', title='Login', form=form)

# create a route for the logout and accounts pages
@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login')) # redirect to the login page and add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login check __init__.py


# create a route for the account page
@users.route("/account", methods=['GET', 'POST']) # create a route for the account page
@login_required # create a route for the account page
def account(): 
    form = UpdateAccountForm()

    if form.validate_on_submit(): # create a route for the account page
        if form.picture.data: # create a route for the account page
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file # update the image file for the current user
        current_user.username = form.username.data # update the username for the current user
        current_user.email = form.email.data # update the email for the current user
        try:
            db.session.commit()  # Commit the changes
            flash('Your account has been updated!', 'success') # Flash a success message
            return redirect(url_for('users.account'))  # Redirect to the account page
        except Exception as e: # Catch any exceptions
            db.session.rollback()  # Rollback in case of error during commit
            flash('An error occurred while updating your account.', 'danger')
            current_app.logger.error(f"Error during commit: {e}")  # Log the error
    elif request.method == 'GET':
        form.username.data = current_user.username # populate the form with the current user's data
        form.email.data = current_user.email # populate the form with the current user's data
    image_file = url_for('static', filename='img/profile_pics/' + current_user.image_file)

    return render_template('account.html', title='Account',
                        image_file=image_file, form=form)


# user posts
@users.route("/user/<string:username>") # create a route for the user page of their posts
def user_posts(username): # define the function for the user page
    page = request.args.get('page', 1, type=int) # get the page number
    user = User.query.filter_by(username=username).first_or_404() # get the user or return 404 if not found
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user, title='User Posts') # render the user posts template


# reset password
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                sender='tahlahbee.institute@gmail.com',
                recipients=[user.email])
    msg.body = render_template('reset_password.txt', token=token)
    msg.html = render_template('reset_password.html', token=token)
    Mail.send(msg)

# reset password route for the user
@users.route("/reset_password", methods=['GET', 'POST']) # create a route for the reset password page
def reset_request(): # define the function for the reset password page
    if current_user.is_authenticated:   # check if the user is authenticated
        return redirect(url_for('main.home')) # redirect to the home page if the user is already authenticated
    form = RequestResetForm()            # create a form for the reset password
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


# reset password route for the user
@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
