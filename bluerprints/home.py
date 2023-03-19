from flask import Blueprint, render_template
from flask_login import login_required, current_user

home = Blueprint("home", __name__)


@home.route("/")
def index():
    return render_template("index.html")


@home.route("/calculate")
def calculate():
    return render_template("result.html")
