from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def user_login():
    return render_template("user_login.html")

@app.route("/user_dashboard")
def user_dashboard():
    return render_template("user_seat_select.html")

if __name__ == "__main__":
    app.debug = True
    app.run()

