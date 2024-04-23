from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
config = Config()


def create_databases(app):
    with app.app_context():
        db.create_all()
