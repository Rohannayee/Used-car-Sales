from flask import Blueprint, render_template, redirect,request, url_for, flash, jsonify
from flask_login import current_user
from app.models import User, Visitor

admin = Blueprint('admin', __name__)

@admin.route('/admin/visitors', methods=['GET'])
def visitors():
    users = User.query.all()
    visitors = Visitor.query.all()
    visitors_size = len(visitors)
    users_size = len(users)
    if current_user.is_authenticated and current_user.is_admin():
        return render_template('admin/visitors.html', users_size=users_size, visitors_size=visitors_size)
    else:
        flash('Please log back', 'danger')
        return redirect(url_for('main.index'))