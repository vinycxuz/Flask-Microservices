from .models import db
from flask import Blueprint, request, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

routes = Blueprint('routes', __name__)

@routes.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
        return None
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    response = jsonify(new_user.toDict())
    response.status_code = 200
    return response
  

@routes.route('/login', method=['GET','POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return None
    login_user(user, remember=remember)
    result = jsonify(user.toDict())
    result.status_code = 200
    return result
