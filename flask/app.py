from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return "Helloooooo! This is the main page <h1>HELLO</h1>"


# =========================== PATH PARAMETER (http://127.0.0.1:5000/Ibrahim) ===========================
@app.route("/<name>/")
def user(name):
    return f"Hello {name} Calculus, you are welcome to this program"


@app.route("/blog/<int:blogId>")                    # Parameter value must be integer
def blog(blogId):
    return f"This is blog with id: {blogId}"


@app.route("/user/", methods=["GET", "POST"])
def user1():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        print(f"Name: {name} Email: {email}")
        return request.form.get("email")
        # return f"<h1>Create New User</h1>"
    else:
        return f"<h1>All users</h1>"


@app.route("/user/<int:id>", methods=["DELETE", "PUT"])
def user_id(id):
    if request.method == "DELETE":
        return f"<h1> Delete User with id: {id}</h1>"
    elif request.method == "PUT":
        return f"<h1> Update User with id: {id} </h1>"
    else:
        return f"This method is not supported"

@app.route("/user/<int:userId>")
def user2(userId):
    return f"User with userId = {userId}"




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
@app.route("/index_page/<name>/<int:age>/")
def index2(name, age):
    return render_template("index2.html", username=name, userage=age, salary=5000, people=["Ibrahim","Musa","Salim","Kate"])


# ----------------------------------------------------
@app.route("/user/create/")
def create():
    return render_template("user/create.html")

# ======================== TEMPLATE INHERITANCE (ie Share a navbar across multiple html files) ======================

# Create the parent template, known as the base template (ie base.html), Check usage in index3.html
@app.route("/index_page3")
def index3():
    return render_template("index3.html")

if __name__ == "__main__":
    app.run(debug=True)