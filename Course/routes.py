from flask import Blueprint, jsonify
from . import db
from .models import Course

routes = Blueprint('routes', __name__)


@routes.route('/courses/title', methods=['GET'])
def get_titles():
    courses = Course.query.all()
    titles = [course.title for course in courses]
    return jsonify({"titles": titles})


@routes.route('/courses/authors', methods=['GET'])
def get_authors():
    courses = Course.query.all()
    authors = [course.author for course in courses]
    return jsonify({"authors": authors})

@routes.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    list = [course for course in courses]
    return jsonify({"courses": list})

