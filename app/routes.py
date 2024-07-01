# app/routes.py

from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db, bcrypt
from app.models import User, Question, Quiz
from flask_login import login_user, current_user, logout_user, login_required

bp = Blueprint('routes', __name__)

@bp.route("/")
@bp.route("/landing")
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    return render_template('landing.html')

@bp.route("/home")
@login_required
def home():
    quizzes = Quiz.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', quizzes=quizzes)

@bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
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
        return redirect(url_for('routes.home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('routes.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'error')
    return render_template('signin.html')

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('routes.landing'))

@bp.route("/create_quiz", methods=['GET', 'POST'])
@login_required
def create_quiz():
    if request.method == 'POST':
        title = request.form.get('title')
        terms = request.form.getlist('terms[]')
        definitions = request.form.getlist('definitions[]')
        quiz = Quiz(title=title, user_id=current_user.id)
        db.session.add(quiz)
        for term, definition in zip(terms, definitions):
            question = Question(term=term, definition=definition, quiz=quiz)
            db.session.add(question)
        db.session.commit()
        flash('Quiz created successfully!', 'success')
        return redirect(url_for('routes.home'))
    return render_template('create_quiz.html')

@bp.route("/delete_quiz/<int:quiz_id>", methods=['POST'])
@login_required
def delete_quiz(quiz_id):
    quiz_to_delete = Quiz.query.get_or_404(quiz_id)
    if quiz_to_delete.user_id != current_user.id:
        flash('You do not have permission to delete this quiz.', 'error')
        return redirect(url_for('routes.home'))
    
    # Delete related Question records first
    Question.query.filter_by(quiz_id=quiz_id).delete()
    
    db.session.delete(quiz_to_delete)
    db.session.commit()
    flash('Quiz deleted successfully!', 'success')
    return redirect(url_for('routes.home'))