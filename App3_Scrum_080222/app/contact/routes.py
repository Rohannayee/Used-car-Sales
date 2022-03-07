from flask import Flask, render_template, redirect, Blueprint, url_for, session, request, jsonify, flash
from .forms import ContactUsForm
contact_view = Blueprint('contact', __name__)

@contact_view.route('/contact', methods=['GET', 'POST'])
def contact_us():
	form = ContactUsForm()
	return render_template('/contact/contact-us.html', form=form)