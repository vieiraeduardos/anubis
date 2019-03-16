from flask import render_template, request, redirect, session

from datetime import date

from app import app

from app.models.Author import Author
from app.models.Admin import Admin


@app.route("/authors/new/", methods=["GET"])
def redirect_new_author():
    user = Admin().getAdminByEmail(session["email"])

    return render_template("new-author.html", user=user)

@app.route("/authors/", methods=["POST"])
def create_author():
    name = request.form.get("name")
    cpf = request.form.get("cpf")
    isStudent = 1 if request.form.get("isStudent") == "1" else 0
    createdAt = str(date.today())
    modifiedAt = str(date.today())
    email = request.form.get("email")

    author = Author(email=email, name=name, cpf=cpf, isStudent=isStudent, createdAt=createdAt, modifiedAt=modifiedAt)

    author.create()

    return redirect("/")
