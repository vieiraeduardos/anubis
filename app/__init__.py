from flask import Flask, render_template

app = Flask(__name__)

from app.controllers import AdminController

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/", methods=["GET"])
def redirect_login():
    return render_template("pages/login-page.html")

@app.route("/signup/", methods=["GET"])
def redirect_login():
    return render_template("pages/register-page.html")
