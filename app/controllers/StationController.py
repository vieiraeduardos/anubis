from flask import render_template, session, request, redirect

from app import app

from app.models.Admin import Admin
from app.models.Station import Station


@app.route("/papers/<paper>/stations/", methods=["GET"])
def redirect_to_station_page(paper):
    user = Admin().getAdminByEmail(session["email"])

    return render_template("stations.html", user=user, paper=paper)


@app.route("/papers/<paper>/stations/", methods=["POST"])
def set_station(paper):
    station = request.form.get("station")
    time = request.form.get("time")
    s = Station(paper=paper, station=station, time=time)

    s.update()

    return redirect("/events/1/")
