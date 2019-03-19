from flask import render_template, request, render_template, redirect, session

from datetime import date

from werkzeug.security import generate_password_hash, check_password_hash

from app import app

from app.models.Judge import Judge
from app.models.Event import Event
from app.models.Paper import Paper
from app.models.Admin import Admin

@app.route("/judges/<code>/")
def edit_judge(code):
    judge = Judge().getJudgeByCode(code)
    user = Admin().getAdminByEmail(session["email"])

    return render_template("edit-judge.html", user=user, judge=judge)

@app.route("/judges/")
def get_judges():
    judges = Judge().getAllJudges()
    user = Admin().getAdminByEmail(session["email"])

    return render_template("list-judges.html", user=user, judges=judges)

@app.route("/judges/events/<code>/", methods=["GET"])
def redirect_to_judge_event(code):
    user = Judge().getJudgeByEmail(session["email"])
    event = Event().getEventByCode(code)
    papers = Paper().getAllPapersByJudge(session["cpf"])

    judges = []

    for paper in papers:
        j = Judge().getAllJudgesByPaper(paper["code"])
        judges.append(j)

    for j in judges:
        for judge in j:
            print(judge["name"])

    return render_template("judge-events.html", user=user, event=event, papers=papers, judges=judges)


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
    user = Admin().getAdminByEmail(session["email"])

    return render_template("new-judge.html", user=user)


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

    return redirect("/judges/new/")


@app.route("/judges/<code>/", methods=["POST"])
def update_judge(code):
    name = request.form.get("name")
    cpf = request.form.get("cpf")
    email = request.form.get("email")

    print(name)
    print(email)

    judge = Judge(name=name, cpf=cpf, email=email)

    judge.update(code)

    return redirect("/judges/")
