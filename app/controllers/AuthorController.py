from flask import render_template, request, redirect

from datetime import date

from app import app

from app.models.Author import Author

@app.route("/authors/new/", methods=["GET"])
def redirect_new_author():
    return render_template("new-author.html")

@app.route("/authors/", methods=["POST"])
def create_author():
    name = request.form.get("name")
    cpf = request.form.get("cpf")
    isStudent = 1 if request.form.get("isStudent") == "1" else 0
    createdAt = str(date.today())
    modifiedAt = str(date.today())

    author = Author(name=name, cpf=cpf, isStudent=isStudent, createdAt=createdAt, modifiedAt=modifiedAt)

    author.create()

    return redirect("/")
