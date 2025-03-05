from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
db = SQLAlchemy()
path = os.getcwd() + '/db.sqlite'
#path = str(os.path.abspath(os.path.join(path, os.pardir)))+"/db.sqlite"


def create_user_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path
    
    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User
    db.init_app(app)
    db.create_all(app=app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import routes
    app.register_blueprint(routes)

    return app
