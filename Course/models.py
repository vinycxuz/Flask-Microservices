from . import db

class Course(db.Model):
    __tablename__="courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    link = db.column(db.String(200), nullable=False)
    image = db.column(db.String(200), nullable=True)


    def __init__(self, title, overview, author, link, image):
        self.id = id
        self.title = title
        self.overview = overview
        self.author = author
        self.link = link
        self.image = image