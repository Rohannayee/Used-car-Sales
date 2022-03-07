from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange




#Card rating sub-system
class ReviewForm(FlaskForm):
	rating = DecimalField(default=0.0, validators=[NumberRange(min=0, max=5), DataRequired()])
	text = TextAreaField('Write a review')
	submit = SubmitField('Review')

class AddCarForm(FlaskForm):
	make = StringField('Car make', validators=[DataRequired()])
	model = StringField(label=("your car model"), validators=[DataRequired(), Length(min=3, message=("Your model name is too short"))])
	name = StringField(label=('Car name'), validators=[DataRequired(), Length(min=3, message=("Your car name is too short"))])
	price = DecimalField(label=("Your car price"), validators=[DataRequired()])
	colour = StringField(label=("your car color"), validators=[DataRequired()])
	age = IntegerField(label=("Age"), validators=[DataRequired()])
	image = FileField('Photo', validators=[FileAllowed(['png', 'jpg'], "Please upload an image")])
	criteria_id = SelectField('Car make', coerce=int)
	submit = SubmitField('Add')

class AddCriteriaForm(FlaskForm):
	type = StringField('your criteria', validators=[DataRequired()])
	submit = SubmitField('Add')
