import os # import the os module to interact with the operating system
import secrets # import the secrets module to generate random strings
from PIL import Image # import the Image module from the PIL library to work with images
from flask import current_app as app # import the current application
from flask import render_template, url_for, flash, redirect, request, abort # import the render_template, url_for, flash, redirect, request modules
from flaskblog import app, db, bcrypt # import the app, db, and bcrypt modules
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm # import the RegistrationForm, LoginForm, and UpdateAccountForm modules
from flaskblog.models import User, Post # import the User and Post modules
from flask_login import login_user, current_user, logout_user, login_required # import the login_user, current_user, logout_user, and login_required modules
from flaskblog.models import Story, Contribution # import the Story and Contribution models
from flaskblog.forms import ContributionForm

# create a route for pages
@app.route("/") # create a route for the home page
@app.route("/home") # create a route for the home page
@login_required #  login required for security
def home(): # define the function for the home page
    post = Post.query.all() # get all posts from the database this is the connector between new post and the database and the home page
    return render_template('home.html', posts=post) # render the home page


@app.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')

# create a route for the register page
@app.route("/register", methods=['GET', 'POST']) # create a route for the register page
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home')) # redirect to the home page if the user is already authenticated
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # generate a hashed password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # pass the username, email, and hashed password to the User model
        db.session.add(user) # db session add the user
        db.session.commit() # commit the db session
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form) #  render the register page

# create a route for the login page
@app.route("/login", methods=['GET', 'POST']) # create a route for the login page
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # check the password hash
            login_user(user, remember=form.remember.data) # login the user
            next_page = request.args.get('next')   # get the next page
            return redirect(next_page) if next_page else redirect(url_for('login')) #  redirect to the next page if it exists
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger') # flash a login unsuccessful message
    return render_template('login.html', title='Login', form=form)

# create a route for the logout and accounts pages
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login')) # redirect to the login page and add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login check __init__.py


# save  picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # generate a random hex string for the filename
    _, f_ext = os.path.splitext(form_picture.filename) # add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/profile_pics', picture_fn) # add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login

    # Resize the image
    output_size = (125, 125) # Adjust the output size as needed
    i = Image.open(form_picture) # open the image
    i.thumbnail(output_size) # resize the image
    i.save(picture_path) # save the image

    return picture_fn # return the filename

@app.route("/account", methods=['GET', 'POST']) # create a route for the account page
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
            return redirect(url_for('account'))  # Redirect to the account page
        except Exception as e: # Catch any exceptions
            db.session.rollback()  # Rollback in case of error during commit
            flash('An error occurred while updating your account.', 'danger')
            app.logger.error(f"Error during commit: {e}")  # Log the error
    elif request.method == 'GET':
        form.username.data = current_user.username # populate the form with the current user's data
        form.email.data = current_user.email # populate the form with the current user's data
    image_file = url_for('static', filename='img/profile_pics/' + current_user.image_file)

    return render_template('account.html', title='Account',
                        image_file=image_file, form=form)



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

# post routes
@app.route("/post/new", methods=['GET', 'POST']) # create a route for the new post page
@login_required
def new_post():
    form = PostForm() # create a form for the new post
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user) # create a new post with the form data
        db.session.add(post) # add the post to the database
        db.session.commit() # commit the changes
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                        form=form, legend='New Post') # render the new post template


@app.route("/post/<int:post_id>") # create a route for the post page
def post(post_id):
    post = Post.query.get_or_404(post_id) # get the post with the given ID or return 404 if not found
    return render_template('post.html', title=post.title, post=post) # render the post template


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST']) # update post
@login_required
def update_post(post_id): # update post
    post = Post.query.get_or_404(post_id) # get the post with the given ID or return 404 if not found
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit(): # validate the form
        post.title = form.title.data # update the title
        post.content = form.content.data # update the content
        db.session.commit() # commit the changes
        flash('Your post has been updated!', 'success') # flash a success message
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET': # populate the form with the current post dat
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                        form=form, legend='Update this Post') # render the update post template


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route('/story-mode', methods=['GET', 'POST']) # create a route for the story mode page
@login_required
def story_mode(): # define the function for the story mode page
    story = Story.query.first()
    if not story:
        story = Story(title="The Start of a Great Adventure", description="An ongoing collaborative story.", author=current_user)
        db.session.add(story)
        db.session.commit()
    form = ContributionForm() # create a form for the contribution
    if form.validate_on_submit():
        contribution = Contribution(content=form.content.data, author=current_user, story=story)
        db.session.add(contribution) # add the contribution to the database
        db.session.commit() # commit the changes
        flash('Your contribution has been added!', 'success')
        return redirect(url_for('story_mode')) # redirect to the story mode page
    contributions = Contribution.query.filter_by(story_id=story.id).order_by(Contribution.date_posted).all()
    return render_template('story_mode.html', title='Story Mode', story=story, contributions=contributions, form=form) # render the story mode template