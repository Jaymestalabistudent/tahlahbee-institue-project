from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404) # 404 error handler
def error_403(error):
    return render_template('errors/403.html'), 403 # Todo: Change the error code to 403 file

@errors.app_errorhandler(404) # 404 error handler
def error_404(error):
    return render_template('errors/404.html'), 404

# create custom error pages

@errors.app_errorhandler(500) # 500 error handler
def error_500(error):
    return render_template('errors/500.html'), 500

