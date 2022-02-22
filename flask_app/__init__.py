from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from flask_app.routes import main

    app.register_blueprint(main)

    return app
