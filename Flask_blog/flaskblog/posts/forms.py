from flask_wtf import FlaskForm  # import the flask form
from wtforms import StringField, SubmitField, TextAreaField # import the string field, password field, submit field and booleanfield textarea field
from wtforms.validators import DataRequired # import the validators

# create a post form to update and delete posts
class PostForm(FlaskForm): # create a post form
    title = StringField('Title', validators=[DataRequired()]) # create a title field
    content = TextAreaField('Content', validators=[DataRequired()]) # create a content field
    submit = SubmitField('Post') # create a submit field

class ContributionForm(FlaskForm):
    content = TextAreaField('Your Contribution', validators=[DataRequired()])
    submit = SubmitField('Add to Story')

