from flask import render_template

from app import app

@app.route("/papers/<code>/evaluations/", methods=["GET"])
def redirect_evaluation_page(code):
    return render_template("new-evaluation.html")
