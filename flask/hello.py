from flask import Flask

app = Flask(__name__)


# RUN: flask --app hello run --debug

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is Ibrahim Musa Calculus</p>"


@app.route("/user/<int:username>")
def userId(username):
    return f"<p>You are welcome {username+12}</p>"