from flask import Blueprint, jsonify, redirect, render_template, request, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("api-request.html")


@views.route("/profile")
def profile():
    args = request.args
    name = args.get("name")
    age = args.get("age")
    return render_template("index.html", name=name, age=age)
    # localhost:8000/profile?name=NAME&age=AGE


@views.route("/json")
def get_json():
    return jsonify({"name": "Raimundo", "age": 42})


@views.route("/data")
def get_data():
    data = {
        "title": "Hello from Flask!",
        "body": "This data was served from a Flask endpoint.",
    }
    return jsonify(data)


@views.route("/go-to-home")
def get_to_home():
    return redirect(url_for("views.home"))
