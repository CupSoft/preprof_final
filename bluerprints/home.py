from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import requests
from algo import algo
from main import db
from models.calcs import Calc


home = Blueprint("home", __name__)


@home.route("/")
def index():
    return render_template("index.html")


# POST save
@home.route("/save", methods=["POST"])
def save_calc():
    input_data = request.form.get("input_data")
    output_data = request.form.get("output_data")

    calc = Calc(input_data=input_data, output_data=output_data)
    db.session.add(calc)
    db.session.commit()

    return render_template(
        "result.html", input_data=input_data, output_data=output_data
    )


@home.route("/calculate")
def calculate():
    if request.args.get("url"):
        url = request.args.get("url")
        token = request.args.get("token")

        headers = {"X-Auth-Token": token}

        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            input_data = r.json()
            output_data = {}

            return render_template(
                "result.html", input_data=input_data, output_data=output_data
            )
        else:
            return render_template("fail.html")
