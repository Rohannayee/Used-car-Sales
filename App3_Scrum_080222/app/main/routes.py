from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User,Visitor
from app import db
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    ip = request.environ['REMOTE_ADDR']
    visitor = Visitor.query.filter_by(ip=ip).first()
    if visitor is None:
        visitor = Visitor(
            ip = ip
        )
        db.session.add(visitor)
        db.session.commit()
    return render_template('index.html',  title='Home')
