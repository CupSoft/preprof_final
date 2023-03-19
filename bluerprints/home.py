from flask import Blueprint, render_template
from flask_login import login_required, current_user

index_bp = Blueprint("home", __name__)


@index_bp.route("/")
def index():
    return render_template("index.html")
