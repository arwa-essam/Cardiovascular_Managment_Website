from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# define the database of the project as an object from SQLAlchemydb = SQLAlchemy()
db = SQLAlchemy()
DB_NAME = "database.db"

# create the app using flask with secret key
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # store the database location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize the database by giving it the app
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # get the database for the website
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# check if the database exists and if not, it creates it
def create_database(app):
    # use it to check that the base path exists
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
