from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdb1.db"

db = SQLAlchemy(app)
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)


with app.app_context():
    db.create_all()



@app.route('/', methods=['GET'])
def home():
    return render_template('user/create.html')

@app.route("/user/", methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        print(f"NAME: {name} EMAIL: {email}")
        
        return redirect(url_for("home"))

    elif request.method == 'GET':
        return "This is a get request"