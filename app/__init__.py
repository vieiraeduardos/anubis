from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.config["SECRET_KEY"] = "@anubis"

from app.controllers import AdminController
from app.controllers import EventController
from app.controllers import AuthorController
from app.controllers import JudgeController
from app.controllers import PaperController

@app.route("/logout/")
def logout():
    session.pop("cpf", "")
    return redirect("/")

@app.route("/")
def index():
    if "cpf" in session:
        if session["type"] == "admin":
            return render_template("admin.html")
        return render_template("judge.html")
    return render_template("index.html")

@app.route("/login/admin/", methods=["GET"])
def redirect_login_admin():
    return render_template("login-page-admin.html")

@app.route("/login/judge/", methods=["GET"])
def redirect_login_judge():
    return render_template("login-page-judge.html")

@app.route("/signup/", methods=["GET"])
def redirect_signup():
    return render_template("register-page.html")
