from datetime import date
from flask import request, render_template


from app import app
from werkzeug.security import generate_password_hash, check_password_hash


from app.models.Admin import Admin


@app.route("/signup/admin/")
def admin_signup():
    cpf = request.form.get("cpf")
    name = request.form.get("name")
    email = request.form.get("email")
    password = generate_password_hash(request.form.get("password"))
    createdAt = str(date.today())
    modifiedAt = str(date.today())

    admin = Admin(cpf=cpf, name=name, email=email, password=password, createdAt=createdAt, modifiedAt=modifiedAt)

    if admin.create():
        return redirect("/login/")
    return render_template("register-page.html")

@app.route("/login/admin/", methods=["POST"])
def admin_login():
    email = request.form.get("email")
    password = request.form.get("password")

    admin = Admin().getAdminByEmail(email)

    if admin:
        if check_password_hash(admin["password"], password):
            session["email"] = admin["email"]
            session["_id"] = admin["_id"]
            session["cpf"] = admin["cpf"]
            return redirect("/")

    error = "E-mail ou senha estão incorretos!"
    return render_template("pages/login-page.html", error=error)
