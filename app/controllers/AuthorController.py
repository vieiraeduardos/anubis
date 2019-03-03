from flask import render_template

from app import app

@app.route("/authors/new/", methods=["GET"])
def redirect_new_author():
    return render_template("new-author.html")
