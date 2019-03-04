from flask import render_template, request, render_template, redirect, session

from datetime import date

from werkzeug.security import generate_password_hash, check_password_hash

from app import app

from app.models.Judge import Judge

@app.route("/login/judge/", methods=["POST"])
def judge_login():
    email = request.form.get("email")
    password = request.form.get("password")

    judge = Judge().getJudgeByEmail(email)

    if judge:
        if check_password_hash(judge["password"], password):
            session["email"] = judge["email"]
            session["cpf"] = judge["cpf"]
            session["type"] = "judge"
            return redirect("/")

    error = "E-mail ou senha estão incorretos!"
    return render_template("login-page-judge.html", error=error)


@app.route("/judges/new/", methods=["GET"])
def redirect_new_judge():
    return render_template("new-judge.html")


@app.route("/judges/", methods=["POST"])
def create_judge():
    name = request.form.get("name")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    password = generate_password_hash(request.form.get("password"))
    createdAt = str(date.today())
    modifiedAt = str(date.today())

    judge = Judge(name=name, cpf=cpf, email=email, password=password, createdAt=createdAt, modifiedAt=modifiedAt)

    judge.create()

    return redirect("/")
