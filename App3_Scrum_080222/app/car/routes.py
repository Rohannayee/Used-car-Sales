from flask import Flask, render_template, redirect, Blueprint, url_for, session, request, jsonify, flash
from app import db
from app.models import Car
from flask_login import current_user
from app.car.forms import AddCarForm, ReviewForm
from app.funcs import save_picture


car= Blueprint('car', __name__)
# a comment
@car.route('/used-vehicles', methods=["GET"])
def cars(cat=None):
	cars = Car.query.all()
	return render_template("car/used-car.html", title="used-vehicles", cars=cars)

@car.route('/used-vehicles/create', methods=["GET", "POST"])
def create():
	if not current_user.is_authenticated:
		flash('please log back', 'warning')
		return redirect(url_for('main.index'))
	form = AddCarForm()
	image = "default.jpg"
	if form.validate_on_submit():
		if request.method == "POST":
			if form.image.data:
				image = save_picture(form.image.data)
			car = Car(
				make = form.make.data,
				model = form.model.data,
				price = form.price.data,
				colour = form.colour.data,
				age = form.age.data,
				image = image
			)
			db.session.add(car)
			db.session.commit()
			flash('Car added succesfully', 'success')
			return redirect(url_for('car.cars'))
	return render_template("/car/create-car.html", title="Add a car", form=form)

@car.route('/car_info/<id>', methods=['GET', 'POST'])
def car_info(id):
	current_car = Car.query.get(id)
	form = ReviewForm()
	return render_template('car/car.html', car=current_car, form=form)