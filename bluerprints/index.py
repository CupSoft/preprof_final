from flask import Blueprint, render_template
from flask_login import login_required, current_user

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    return render_template("index.html")


@index_bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)
