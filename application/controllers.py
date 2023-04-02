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

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")
