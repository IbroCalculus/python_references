from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO</h1>"


# =========================== PATH PARAMETER (http://127.0.0.1:5000/Ibrahim) ===========================
@app.route("/<name>/")
def user(name):
    return f"Hello {name}, you are welcome to this program"


# ============================== REDIRECT =============================
@app.route("/from_redirect/")
def redirected():
    return "<h1>Redirect Page</h1> <p>This is coming from the redirect route</p>"

# http://127.0.0.1:5000/admin/  (REDIRECT TO THE ABOVE FUNCTION)
@app.route("/admin/")
def admin():
    return redirect(url_for("redirected"))        # Where "redirected" is the function name in the above @app.route("/from_redirect/")


# http://127.0.0.1:5000/Calculus/   (REDIRECT TO A FUNCTION THAT ACCEPTS ARGUMENT ABOVE (@app.route("/<name>/")) )
@app.route("/admin/<name>/")
def admin_user(name):
    return redirect(url_for("user", name=name))     # Where name is the argument name in the above function



# ==================== TEMPLATES ========================
# Create a 'templates' to contain the html files

# http://127.0.0.1:5000/index_page/
@app.route("/index_page/")
def index():
    return render_template("index.html")

# Passing dynamic information in the rendered html file
# http://127.0.0.1:5000/index_page/Ibrahim/56/
@app.route("/index_page/<name>/<age>/")
def index2(name, age):
    return render_template("index2.html", username=name, userage=age, salary=5000, people=["Ibrahim","Musa","Salim","Kate"])




# ======================== TEMPLATE INHERITANCE (ie Share a navbar across multiple html files) ======================

# Create the parent template, known as the base template (ie base.html), Check usage in index3.html
@app.route("/index_page3")
def index3():
    return render_template("index3.html")