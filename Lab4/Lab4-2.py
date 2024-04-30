from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User, connect_db

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Signup logic here
        return redirect(url_for('.login'))

    return render_template('signup.html')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login logic here
        return redirect(url_for('.protected'))

    return render_template('login.html')

@auth_blueprint.route('/protected')
@login_required
def protected():
    # Protected logic here
    return render_template('protected.html', books=[])

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
