from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from settings import settings

db = SQLAlchemy()


app = Flask(__name__)

app.config["SECRET_KEY"] = settings.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = settings.DB_URL

db.init_app(app)


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

from models.users import User

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Blueprints
from bluerprints import auth as auth_blueprint
from bluerprints import index as index_blueprint

app.register_blueprint(auth_blueprint.auth)
app.register_blueprint(index_blueprint.index_bp)
