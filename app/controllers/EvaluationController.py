from flask import redirect, render_template, request, session

from app import app

from app.models.Evaluation import Evaluation
from app.models.Paper import Paper
from app.models.Link import Link

@app.route("/papers/<code>/evaluations/", methods=["GET"])
def redirect_evaluation_page(code):
    paper = Paper().getPaperByCode(code)

    return render_template("new-evaluation.html", code=code, paper=paper)

@app.route("/papers/<paper>/evaluations/", methods=["POST"])
def evaluate(paper):
    originality = request.form.get("originality")
    consistency = request.form.get("consistency")
    clarity = request.form.get("clarity")
    relevance = request.form.get("relevance")
    quality = request.form.get("quality")
    domain = request.form.get("domain")
    judge = session["cpf"]

    eval = Evaluation(paper=paper, judge=judge, originality=originality, consistency=consistency, clarity=clarity, relevance=relevance, quality=quality, domain=domain)

    eval.create()

    link = Link()
    link.updateStatus(judge=judge, paper=paper)

    return redirect("/")
