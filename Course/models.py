from . import db

class Course(db.Model):
    __tablename__="courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=True)


    def __init__(self, id, title, overview, author, link, image):
        self.id = id
        self.title = title
        self.overview = overview
        self.author = author
        self.link = link
        self.image = image
        
