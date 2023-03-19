from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import settings

db = SQLAlchemy()


app = Flask(__name__)

app.config["SECRET_KEY"] = settings.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = settings.DB_URL

db.init_app(app)


from models.calcs import Calc

with app.app_context():
    db.create_all()


# Blueprints
from bluerprints import home as home_blueprint

app.register_blueprint(home_blueprint.home)
