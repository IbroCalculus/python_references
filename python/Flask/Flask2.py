from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# ============= RENDER AN HTML DOCUMENT ================

# @app.route('/')
# def home():
#     return render_template('index.html')


# ============= RENDER AN HTML DOCUMENT, ALSO PASSING IN PARAMETER ================

@app.route('/<paramPassed>/<fName>/<sName>')
def home(paramPassed, fName, sName):
    return render_template('index.html', content=paramPassed, fName=fName, sName=sName)   #Check: Tech with Tim, tutorial 2




if __name__ == '__main__':
    app.run()