from flask import Flask, request
from flask import render_template
from flask import current_app as app
# from application.models import Article



@app.route("/", methods = ["GET", "POST"])
def user_login():
    return render_template("user_login.html")

@app.route("/user_dashboard")
def user_dashboard():
    return render_template("user_dashboard.html")

@app.route("/user_bookings")
def user_bookings():
    return render_template("user_bookings.html")

@app.route("/user_seat_selection")
def user_seat_selection():
    return render_template("user_seat_selection.html")

@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/admin_show_summary")
def admin_show_summary():
    return render_template("admin_show_summary.html")

@app.route("/admin_shows")
def admin_shows():
    return render_template("admin_shows.html")

@app.route("/admin_venues")
def admin_venues():
    return render_template("admin_venues.html")