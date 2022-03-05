from flask import Flask, render_template, redirect, Blueprint, url_for, session, request, jsonify
from app import db
from app.models import Car
from app.car.forms import AddCarForm, ReviewForm
from app.funcs import save_picture


car= Blueprint('car', __name__)
# a comment
@car.route('/used-vehicles', methods=["GET"])
def cars(cat=None):
	return render_template("car/used-car.html", title="used-vehicles")

@car.route('/used-vehicles/create', methods=["GET", "POST"])
def add_car():
	form = AddCarForm()
	image = "default.jpg"
	if form.validate_on_submit():
		if request.methods == "POST":
			if form.data.image:
				image = save_picture(form.data.image)
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
			return redirect(url_for('car.add_car'))
	return render_template("/car/create-car.html", title="Add a car", form=form)

