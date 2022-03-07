from flask import Flask, render_template, redirect, Blueprint, url_for, session, request, jsonify, flash
from app import db
from app.models import Criteria
from flask_login import current_user
from app.criteria.forms import AddCriteriaForm

criteria_view = Blueprint('criteria', __name__)

@criteria_view.route('/criteria', methods=['GET'])
def criteria():
	criterias = Criteria.query.all()
	return render_template('criteria/criteria.html', criterias=criterias)

@criteria_view.route('/criteria/create', methods=['GET', 'POST'])
def create_criteria():
	if not current_user.is_authenticated:
		flash('please log back', 'warning')
		return redirect(url_for('main.index'))
	form = AddCriteriaForm()
	if form.validate_on_submit():
		if request.method == "POST":
			criteria = Criteria(
				type = form.type.data
			)
			db.session.add(criteria)
			db.session.commit()
			flash('Successfully added a criteria', 'success')
			return redirect(url_for('criteria.criteria'))
	return render_template('criteria/create_criteria.html', form=form)