from flask import render_template

from app import app

from app.models.Event import Event
from app.models.Paper import Paper
from app.models.Evaluation import Evaluation

@app.route("/events/<code>/processing/", methods=["GET"])
def redirect_processing(code):
    papers = Paper().getAllPapers()

    for paper in papers:
        note = Evaluation().getNoteByPaper(paper.code)
        paper.update({"note": note})

    return render_template("processing.html", papers=papers)

@app.route("/events/<code>/", methods=["GET"])
def redirect_event_page(code):
    event = Event().getEventByCode(code)
    papers = Paper().getAllPapers()

    return render_template("admin-events.html", event=event, papers=papers)
