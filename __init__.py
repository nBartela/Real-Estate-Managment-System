from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_pyfile('../config.py')
    login_manager.init_app(app)
    from .routes import main
    app.register_blueprint(main)

    return app