from flask import Flask
#NB: Check Tech with Tim as reference




app = Flask(__name__)


@app.route('/')
def index():
    return "HELLO IBRAHIM! This is the homePage <h1> This is a header 1 header</h1> <a href="" target="">Google</a>"


if __name__ == '__main__':
    app.run()