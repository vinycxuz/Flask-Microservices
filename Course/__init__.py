from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

path = os.getcwd()+"/db.sqlite"

def create_course_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path

    db.init_app(app)
    from .models import Course
    #db.create_all(app=app)

    from .routes import routes as route_blueprint
    app.register_blueprint(route_blueprint)
    return app