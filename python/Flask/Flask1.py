from flask import Flask, redirect, url_for


#NB: Check Tech with Tim as reference
# Flask is a micro web framework for building websites with python


app = Flask(__name__)


#Each function define a page on the website

@app.route('/')         #'/' This implies this is the index.html (home page)
def index():
    return "HELLO IBRAHIM! This is the homePage <h1> This is a header 1 header</h1> <a href="" target="">Google</a>"


#NB @app.route('/homePage1/'). This will allow the page to be accessed with or without / at the end. ie homePage1/
@app.route('/homePage1')         #'.../homePage1' will navigate us to this page
def homePage1():
    return "Welcome to homePage2"


@app.route('/<pageID>')          #Take's in a string parameter for both the URL and the the function
def pageX1(pageID):
    return f'This is page with string parameter: {pageID}'


@app.route('/<int:pageID2>')          #Take's in an int parameter for both the URL and the the function
def pageX2(pageID2):
    return f'This is page with integer parameter: {pageID2}'


@app.route('/adminPage')        #This is for redirecting. E.g: When access is not granted to visit this page
def adminPage():
    return redirect(url_for('index'))   #'index' is the name of the function, not '/...'


@app.route('/adminPage2')        #This is for redirecting to a page that takes in parameter.
def adminPage2():
    return redirect(url_for('pageX1', pageID="Redirected from admin page"))   #'index' is the name of the function, not '/...'


# For this file not to be clustered, check Flask2.py for more



if __name__ == '__main__':
    app.run()