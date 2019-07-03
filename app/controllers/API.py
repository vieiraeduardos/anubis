from flask import jsonify, request

from app import app

from app.models.Event import Event
from app.models.Paper import Paper
from app.models.Evaluation import Evaluation
from app.models.Link import Link
from app.models.Judge import Judge

#Listando todos os eventos pertecentes a um avaliador
@app.route("/api/events/", methods=["GET"])
def api_get_all_events():
    events = Event().getAllEvents()

    result = {
        "events": events
    }

    return jsonify(result)

#Listando todos os papéis pertecentes a um avaliador
@app.route("/api/papers/", methods=["GET"])
def api_get_all_papers():
    papers = Paper().getAllPapers()

    result = {
        "papers": papers
    }

    return jsonify(result)

#Listando um paper individual
@app.route("/api/papers/<code>/", methods=["GET"])
def get_paper(code):
    paper = Paper().getPaperByCode(code)

    result = {
        "paper": paper
    }

    return jsonify(result)

#Avaliar paper
@app.route("/api/papers/<paper>/evaluations/", methods=["POST"])
def api_evaluate(paper):
    try:
        originality = request.form.get("originality")
        consistency = request.form.get("consistency")
        clarity = request.form.get("clarity")
        relevance = request.form.get("relevance")
        quality = request.form.get("quality")
        domain = request.form.get("domain")
        judge = request.form.get("cpf")

        eval = Evaluation(paper=paper, judge=judge, originality=originality, consistency=consistency, clarity=clarity, relevance=relevance, quality=quality, domain=domain, presenter="")

        eval.create()

        link = Link()
        link.updateStatus(judge=judge, paper=paper)

        return "OK"
    except:
        return "Erro"
