from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange


class ContactUsForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('email address', validators=[DataRequired(), Email()])
	text = TextAreaField('your suggestion', validators=[DataRequired()])
	submit = SubmitField('Send')