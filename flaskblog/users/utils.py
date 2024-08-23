
import os
import secrets # import the secrets module to generate random strings
from PIL import Image # import the Image module from the PIL library to work with images
from flask import current_app as app

# save  picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # generate a random hex string for the filename
    _, f_ext = os.path.splitext(form_picture.filename) # add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/img/profile_pics', picture_fn) # add headers to prevent caching of the website so it doesn't refresh the page or go back after logout or login

    # Resize the image
    output_size = (125, 125) # Adjust the output size as needed
    i = Image.open(form_picture) # open the image
    i.thumbnail(output_size) # resize the image
    i.save(picture_path) # save the image

    return picture_fn # return the filename
