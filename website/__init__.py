from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# if os.path.exists('envy.py'):
#     import env

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # app.secret_key = os.environ.get("SECRET_KEY")
    app.config['SECRET_KEY'] = 'secretkey for the project'
    # Tell  where to create the database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import .models, so we load this file and it runs
    # to define the classes it contains before we create the database
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    """
    Check if the database exist and if not, creates it.
    website correspond to the name of the folder.
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
