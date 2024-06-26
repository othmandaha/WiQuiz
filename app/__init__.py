# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'routes.signin'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Adjust as needed

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app import routes

    app.register_blueprint(routes.bp)

    with app.app_context():
        db.create_all()  # Ensure all tables are created

    return app

