from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(32), nullable=False)


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    


