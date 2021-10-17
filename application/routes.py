from application import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/courses")
def courses():
    return render_template("not_implemented_yet.html")


@app.route("/register")
def register():
    return render_template("not_implemented_yet.html")


@app.route("/login")
def login():
    return render_template("not_implemented_yet.html")
