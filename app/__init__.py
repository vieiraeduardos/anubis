from flask import Flask, render_template, session, redirect

app = Flask(__name__, static_folder='static', static_url_path='')

app.config["SECRET_KEY"] = "@anubis"

from app.controllers import AdminController
from app.controllers import EventController
from app.controllers import AuthorController
from app.controllers import JudgeController
from app.controllers import PaperController
from app.controllers import EvaluationController
from app.controllers import LinkController
from app.controllers import StationController
from app.controllers import PrinterController


from app.models.Judge import Judge
from app.models.Admin import Admin

@app.route("/logout/")
def logout():
    session.pop("cpf", "")
    return redirect("/")

@app.route("/")
def index():
    if "cpf" in session:
        if session["type"] == "admin":
            user = Admin().getAdminByEmail(session["email"])
            return render_template("admin.html", user=user)
        user = Judge().getJudgeByEmail(session["email"])
        return render_template("judge.html", user=user)
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
