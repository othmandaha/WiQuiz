# app/routes.py

from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db, bcrypt
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required

bp = Blueprint('routes', __name__)

@bp.route("/")
@bp.route("/landing")
def landing():
    return render_template('landing.html')

@bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('routes.landing'))
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('routes.signup'))
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already used.', 'error')
            return redirect(url_for('routes.signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('routes.signin'))

    return render_template('signup.html')

@bp.route("/signin", methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('routes.landing'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('routes.landing'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'error')
    return render_template('signin.html')

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('routes.landing'))
