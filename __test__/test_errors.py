from flask import Flask

def create_app():
    app = Flask(__name__)

    # Define basic error handlers
    @app.errorhandler(404)
    def error_404(error):
        return "404 Not Found", 404

    @app.errorhandler(500)
    def error_500(error):
        return "500 Internal Server Error", 500

    # Add routes for testing purposes
    @app.route('/cause-error')
    def cause_error():
        raise Exception("This is a test exception for 500 error")

    return app
