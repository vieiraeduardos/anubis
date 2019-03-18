from flask import redirect, render_template, request, session

from app import app

from app.models.Evaluation import Evaluation
from app.models.Paper import Paper
from app.models.Link import Link
from app.models.Judge import Judge


@app.route("/judges/<judge>/papers/<paper>/evaluations/", methods=["GET"])
def redirect_edit_evaluation(judge, paper):
    evaluation = Evaluation().getEvaluation(judge=judge, paper=paper)
    user = Judge().getJudgeByEmail(session["email"])
    paper = Paper().getPaperByCode(paper)

    authors = paper["autores"].split(",")

    return render_template("edit-evaluation.html", evaluation=evaluation, user=user, authors=authors)

@app.route("/judges/<judge>/papers/<paper>/evaluations/", methods=["POST"])
def update_evaluation(judge, paper):
    originality = request.form.get("originality")
    consistency = request.form.get("consistency")
    clarity = request.form.get("clarity")
    relevance = request.form.get("relevance")
    quality = request.form.get("quality")
    domain = request.form.get("domain")
    presenter = request.form.get("presenter")

    eval = Evaluation(paper=paper, judge=judge, originality=originality, consistency=consistency, clarity=clarity, relevance=relevance, quality=quality, domain=domain, presenter=presenter)

    eval.update()

    user = Judge().getJudgeByEmail(session["email"])

    return render_template("messages/success-evaluation.html", user=user)


@app.route("/papers/<code>/evaluations/", methods=["GET"])
def redirect_evaluation_page(code):
    paper = Paper().getPaperByCode(code)
    user = Judge().getJudgeByEmail(session["email"])

    authors = paper["autores"].split(",")

    return render_template("new-evaluation.html", code=code, paper=paper, user=user, authors=authors)

@app.route("/papers/<paper>/evaluations/", methods=["POST"])
def evaluate(paper):
    originality = request.form.get("originality")
    consistency = request.form.get("consistency")
    clarity = request.form.get("clarity")
    relevance = request.form.get("relevance")
    quality = request.form.get("quality")
    domain = request.form.get("domain")
    judge = session["cpf"]
    presenter = request.form.get("presenter")

    eval = Evaluation(paper=paper, judge=judge, originality=originality, consistency=consistency, clarity=clarity, relevance=relevance, quality=quality, domain=domain, presenter=presenter)

    eval.create()

    link = Link()
    link.updateStatus(judge=judge, paper=paper)

    return render_template("messages/success-evaluation.html", user=user)
