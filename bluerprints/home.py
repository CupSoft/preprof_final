from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
import requests
from algo import algo
from main import db
from models.calcs import Calc


home = Blueprint("home", __name__)

@home.route("/saves")
def saves():
    allsaves = Calc.query.all()

    return render_template("saves.html", allsaves=allsaves)


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

    return redirect("http://0.0.0.0:8000/")


@home.route("/calculate")
def calculate():
    if request.args.get("url"):
        url = request.args.get("url")
        token = request.args.get("token")

        headers = {"X-Auth-Token": token}

        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            input_data = r.json()["message"]
            input_data = input_data[int(request.args.get("testnum"))]["points"]
            print(input_data)
            output_data = algo.process_mission(input_data)

            dayinfo = 'инфа не запрашивается'

            if not (request.args.get("day_input") is None):
                for i in output_data[0]:
                    if i.num == int(request.args.get("day_input")):
                        dayinfo = i

                        
                

            return render_template(
                "result.html", input_data=input_data, output_data=output_data, dayinfo=dayinfo
            )
        else:
            return render_template("fail.html")


