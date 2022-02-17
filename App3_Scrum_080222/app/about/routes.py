from flask import Flask, render_template, url_for, Blueprint

about = Blueprint('about', __name__)

@about.route('/about')
def about_us():
	return render_template('about/about.html')