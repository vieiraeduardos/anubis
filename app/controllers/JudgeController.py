from flask import render_template

from app import app

@app.route("/judges/new/", methods=["GET"])
def redirect_new_judge():
    return render_template("new-judge.html")
