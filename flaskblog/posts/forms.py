import unittest
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# Define the forms as provided
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class ContributionForm(FlaskForm):
    content = TextAreaField('Your Contribution', validators=[DataRequired()])
    submit = SubmitField('Add to Story')