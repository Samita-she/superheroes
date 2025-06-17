from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")  # Or however you named your config

    db.init_app(app)

    from .routes import api
    app.register_blueprint(api)

    return app
