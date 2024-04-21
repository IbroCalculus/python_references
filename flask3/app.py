from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy


app = Flask(__name__)
app.secret_key = "session_secret_key"
app.permanent_session_lifetime = timedelta(days=5)      # Set how long the session lasts

@app.route("/")
def root():
    return render_template("index2.html")

# @app.route("/<name>")
# def home(name):
#     return render_template("index.html", name=name)

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form.get("nm")
        session["user"] = user
        flash("Login successful")
        # return redirect(url_for("user", usr=user))
        return redirect(url_for("user2"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user2"))
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<p>Hello {usr}</p>"


@app.route("/user")
def user2():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return render_template("login.html")

@app.route("/logout/")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)

    return redirect(url_for("login"))

# @app.route("/<user>/")
# def user(user):
#     return f"<p>Hello {user}</p>"
#
# @app.route("/admin/")
# def admin():
#     print("You just accessed the admin page")
#     return redirect(url_for("user", user="Calculus"))







if __name__ == "__main__":
    app.run(debug=True)