from flask import render_template, request, redirect, session
from app import app

from app.models.Paper import Paper
from app.models.Judge import Judge
from app.models.Link import Link
from app.models.Admin import Admin

@app.route("/papers/<paper>/links/<code>/remove/")
def remove_link(paper, code):
    link = Link()
    link.remove(code)

    return redirect("/events/1/")

@app.route("/links/", methods=["POST"])
def link_judge_to_paper():
    judge = request.form.get("judge")
    paper = request.form.get("paper")

    link = Link(judge=judge, paper=paper)

    if(link.isComplete()):
        if(link.alreadyExists()):
            link = Link(judge=judge, paper=paper)
            link.create()
            return redirect("/events/1/")
        else:
            error="O avaliador já foi selecionado para avaliar este trabalho!"
    else:
        error="O trabalho selecionado já possui o limite máximo de avaliadores!"

    papers = Paper().getAllPapers()
    judges = Judge().getAllJudges()
    user = Admin().getAdminByEmail(session["email"])

    return render_template("link-judge.html", papers=papers, judges=judges, user=user, error=error)


@app.route("/papers/<paper>/links/", methods=["GET"])
def get_redirect_link(paper):
    judges = Judge().getAllJudges()
    user = Admin().getAdminByEmail(session["email"])


    return render_template("link-judge.html", paper=paper, judges=judges, user=user)
