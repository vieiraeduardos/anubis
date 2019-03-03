from flask import render_template

from app import app

@app.route("/events/new/", methods=["GET"])
def redirect_new_paper():
    return render_template("new-paper.html")
