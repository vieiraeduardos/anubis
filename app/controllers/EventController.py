import operator

from flask import render_template, session

from app import app

from app.models.Event import Event
from app.models.Paper import Paper
from app.models.Evaluation import Evaluation
from app.models.Admin import Admin
from app.models.Link import Link


def ordenar(papers):
    for i in range(len(papers)):

        min_idx = i
        for j in range(i+1, len(papers)):
            if int(papers[min_idx]["note"]) < int(papers[j]["note"]):
                min_idx = j

        papers[i], papers[min_idx] = papers[min_idx], papers[i]

    return papers

@app.route("/events/<code>/processing/", methods=["GET"])
def redirect_processing(code):
    papers = Paper().getAllPapers()
    user = Admin().getAdminByEmail(session["email"])


    for paper in papers:
        note = Evaluation().getNoteByPaper(paper["code"])
        if(note["total"] == None):
            note["total"] = 0

        paper.update({"note": round(note["total"], 2) })

    papers = ordenar(papers)

    return render_template("processing.html", papers=papers, user=user)

@app.route("/events/<code>/", methods=["GET"])
def redirect_event_page(code):
    event = Event().getEventByCode(code)
    papers = Paper().getAllPapers()
    user = Admin().getAdminByEmail(session["email"])
    links = Link().getAllLinks()

    return render_template("admin-events.html", event=event, papers=papers, user=user, links=links)
