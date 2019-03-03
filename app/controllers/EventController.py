from flask import render_template

from app import app

from app.models.Event import Event

@app.route("/events/<code>/", methods=["GET"])
def redirect_event_page(code):
    event = Event().getEventByCode(code)

    return render_template("admin-events.html", event=event)

@app.route("/events/new/", methods=["GET"])
def redirect_new_paper():
    return render_template("new-paper.html")
