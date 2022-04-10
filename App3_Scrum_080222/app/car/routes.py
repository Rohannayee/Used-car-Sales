from flask import Flask, render_template, redirect, Blueprint, url_for, session, request, jsonify, flash
from app import db
from app.models import Car,Review, Criteria
from flask_login import current_user
from app.car.forms import AddCarForm, ReviewForm
from app.funcs import save_picture


car= Blueprint('car', __name__)
# a comment
@car.route('/used-vehicles/', methods=['GET'])
@car.route('/used-vehicles/<cat>/<t>', methods=["GET"])
def cars(cat=None, t=None):
	cars = Car.query.all()
	criterias = [c for c in Criteria.query.all()]
	models = [car.model for car in Car.query.all()]
	if cat is not None and t is not None:
		if t == "model":
			cars = [c for c in Car.query.filter_by(model=cat)]
		elif t == "make":
			cars = [c for c in Car.query.filter_by(make=cat)]
	elif request.args.get('number1') is not None and request.args.get('number2') is not None:
		number1 = float(request.args.get('number1'))
		number2 = float(request.args.get('number2'))
		cars = [c for c in Car.query.all() if c.price >= number1 and c.price <= number2]
		if cars.count == 0:
			flash(f"{cars.count} found from records",'danger')
		flash(f"{cars.count} found from records", 'success')
	return render_template("car/used-car.html", title="used-vehicles", cars=cars, models=models, criterias=criterias)

@car.route('/used-vehicles/create', methods=["GET", "POST"])
def create():
	if not current_user.is_authenticated:
		flash('please log back', 'warning')
		return redirect(url_for('main.index'))
	form = AddCarForm()
	form.criteria_id.choices = [(c.id, c.type) for c in Criteria.query.all()]
	image = "default.jpg"
	if form.validate_on_submit():
		if request.method == "POST":
			if form.image.data:
				image = save_picture(form.image.data)
			car_make = form.make.data.lower()
			car = Car(
				make = car_make,
				model = form.model.data,
				price = form.price.data,
				name = form.name.data,
				colour = form.colour.data,
				history = form.history.data,
				age = form.age.data,
				image = image,
				criteria_id = form.criteria_id.data
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
	if form.validate_on_submit():
		if request.method == "POST":
			stored_review = Review.query.filter_by(user_id=current_user.id).first()
			if stored_review is not None:
				flash("Cannot review a car twice!!")
				return redirect(url_for('car.car_info', id=id))
			review = Review(
				rating = form.rating.data,
				text = form.text.data,
				user_id = current_user.id,
				car_id = id
			)
			db.session.add(review)
			db.session.commit()
			flash("Your review has been added")
			return redirect(url_for('car.car_info'))
	return render_template('car/car.html', car=current_car, form=form)