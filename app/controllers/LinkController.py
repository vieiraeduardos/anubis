from flask import render_template, request, redirect
from app import app

from app.models.Paper import Paper
from app.models.Judge import Judge
from app.models.Link import Link

@app.route("/links/", methods=["POST"])
def link_judge_to_paper():
    judge = request.form.get("judge")
    paper = request.form.get("paper")

    link = Link(judge=judge, paper=paper)

    link.create()

    return redirect("/")

@app.route("/links/", methods=["GET"])
def get_redirect_link():
    papers = Paper().getAllPapers()
    judges = Judge().getAllJudges()

    return render_template("link-judge.html", papers=papers, judges=judges)
