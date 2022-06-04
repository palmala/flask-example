from unittest.util import _MAX_LENGTH
from application import app
from application import db
from flask import render_template



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index = True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    courses_list = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]
    return render_template("courses.html", courses_list=courses_list, courses = True, term = term)


@app.route("/register")
def register():
    return render_template("register.html", register = True)


@app.route("/login")
def login():
    return render_template("login.html", login = True)


class User(db.Document):
    user_id     = db.IntField(unique=True)
    first_name  = db.StringField(max_length=50)
    last_name   = db.StringField(max_length=50)
    email       = db.StringField(max_length=30)
    password    = db.StringField(max_length=30)

@app.route("/user")
def user():
    # User(user_id=1, first_name="John", last_name="Smith", email="a@b.hu", password="123").save()
    # User(user_id=2, first_name="Jane", last_name="Smith", email="asdasd@ds.hu", password="123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
