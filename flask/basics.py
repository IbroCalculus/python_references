# If your main Python file is named app.py or wsgi.py. Flask looks for these filenames by default...
# To run: flask run     (url is : http://127.0.0.1:5000, where 5000 is default port)
# To change port: flask run --port=5001
# To run in debug mode: flask run --port=5001 --debug    (This is like --reload in FastApi, ie; on saving, it applies changes)

# --- If file is saved with a different title apart from app.py or wsgi.py, ie hello.py, run as thus:
# flask --app hello run --debug

# Or include this at the base of the app.py page to enable run by clicking on the run command in the IDE. or via cmd command: python "python_filename.py"
'''
if __name__ == "__main__":
    app.run(debug=True)                               # Default
    app.run(host='0.0.0.0', port=8080)
'''


# IMAGE: Check index.html to see how image was passed

# CSS STYLESHEET: Check index.html header section to see how to link a css file

# DATABASE: pip install flask-sqlalchemy
# Check flask2/app.py and flask3/app for usage

# To extract the routes into a single file, create a package inside the application titled __init__.py.
# ie Created it inside a folder 'app' from the root directory. This file is always ran without calling. Check it.