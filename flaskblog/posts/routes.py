from flask import render_template, url_for, flash, redirect, request, abort, Blueprint # import the render_template, url_for, flash, redirect, request modules
from flask_login import current_user, login_required # import the current user
from flaskblog import db # import the db
from flaskblog.models import Post, Story, Contribution # import the user model
from flaskblog.posts.forms import PostForm, ContributionForm # import the post form

posts = Blueprint('posts', __name__) # create a blueprint for the posts module



# post routes
@posts.route("/post/new", methods=['GET', 'POST']) # create a route for the new post page
@login_required
def new_post():
    form = PostForm() # create a form for the new post
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user) # create a new post with the form data
        db.session.add(post) # add the post to the database
        db.session.commit() # commit the changes
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                        form=form, legend='New Post') # render the new post template


@posts.route("/post/<int:post_id>") # create a route for the post page
def post(post_id):
    post = Post.query.get_or_404(post_id) # get the post with the given ID or return 404 if not found
    return render_template('post.html', title=post.title, post=post) # render the post template


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST']) # update post
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
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET': # populate the form with the current post dat
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                        form=form, legend='Update this Post') # render the update post template


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route('/story-mode', methods=['GET', 'POST']) # create a route for the story mode page
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
        return redirect(url_for('posts.story_mode')) # redirect to the story mode page
    contributions = Contribution.query.filter_by(story_id=story.id).order_by(Contribution.date_posted).all()
    return render_template('story_mode.html', title='Story Mode', story=story, contributions=contributions, form=form) # render the story mode template


