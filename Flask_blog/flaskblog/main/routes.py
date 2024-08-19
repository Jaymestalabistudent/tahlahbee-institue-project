from flask import render_template, request, Blueprint # import the render_template, url_for, flash, redirect, request modules
from flaskblog.models import Post # import the User,Post, story and Contribution models
from flask_login import current_user, login_required # import the current user

main = Blueprint('main', __name__) # create a blueprint for the posts module

# create a route for pages
@main.route("/") # create a route for the home page
@main.route("/home") # create a route for the home page
@login_required #  login required for security
def home(): # define the function for the home page
    try:
        page = int(request.args.get('page', 1))  # Get page and ensure it's an integer
    except ValueError:
        page = 1  # Default to page 1 if conversion fails
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3) # get the posts with the given page number
    return render_template('home.html', posts=post) # render the home page


@main.route("/about")
def about():
    return render_template('about.html', title='About')

# additional routes
@main.route("/tahlahbee")
def tahlahbee():
    return render_template('tahlahbee.html', title = 'test page')

@main.route("/info")
@login_required
def info():
    return render_template('info.html', title = 'Information')

@main.route("/spotify")
@login_required
def spotify():
    return render_template('spotify.html', title = 'Music and Podcast')

@main.route("/video")
@login_required
def video():
    return render_template('video.html', title = 'Movies and Series')

@main.route("/events")
@login_required
def events():
    return render_template('events.html', title = 'Meet with us')

