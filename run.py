from flaskblog import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(host='0.0.0.0', port=5432)