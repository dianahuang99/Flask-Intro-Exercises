from flask import Flask

app = Flask(__name__)


@app.route("/welcome/<hb>")
def welcome(hb):
    if hb == "home":
        return "welcome home"
    elif hb == "back":
        return "welcome back"


@app.route("/welcome")
def welcome_start():
    return "welcome"

