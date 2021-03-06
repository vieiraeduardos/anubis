from flask import render_template, request, redirect, session

from datetime import date

from app import app

from app.models.Author import Author
from app.models.Category import Category
from app.models.Subcategory import Subcategory
from app.models.Paper import Paper
from app.models.Admin import Admin
from app.models.Judge import Judge

@app.route("/papers/<code>/", methods=["GET"])
def redirect_edit_paper(code):
    paper = Paper().getPaperByCode(code)
    user = Admin().getAdminByEmail(session["email"])
    judges = Judge().getAllJudgesByPaper(code);

    return render_template("edit-paper.html", paper=paper, user=user, judges=judges)

@app.route("/papers/new/", methods=["GET"])
def redirect_new_paper():
    authors = Author().getAllAuthors()
    categories = Category().getAllCategories()
    subcategories = Subcategory().getAllSubcategories()
    user = Admin().getAdminByEmail(session["email"])

    return render_template("new-paper.html", authors=authors, categories=categories, subcategories=subcategories, user=user)


@app.route("/papers/", methods=["POST"])
def create_paper():
    title = request.form.get("title")
    abstract = request.form.get("abstract")
    author = request.form.get("author")
    category = request.form.get("category")
    subcategory = request.form.get("subcategory")
    createdAt = str(date.today())
    modifiedAt = str(date.today())

    paper = Paper(title=title, abstract=abstract, author=author, isExposed=0, isPresented=0, category=category, subcategory=subcategory, createdAt=createdAt, modifiedAt=modifiedAt)

    paper.create()

    return redirect("/")
