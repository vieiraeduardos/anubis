from flask import Flask, render_template, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "@anubis"

from app.controllers import AdminController
from app.controllers import EventController


@app.route("/")
def index():
    if "cpf" in session:
        if session["type"] == "admin":
            return render_template("admin.html")
        return render_template("judge.html")
    return render_template("index.html")

@app.route("/login/", methods=["GET"])
def redirect_login():
    return render_template("login-page.html")

@app.route("/signup/", methods=["GET"])
def redirect_signup():
    return render_template("register-page.html")
