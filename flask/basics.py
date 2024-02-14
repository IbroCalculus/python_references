# Ensure that your main Python file is named app.py or wsgi.py. Flask looks for these filenames by default...
# To run: flask run     (url is : http://127.0.0.1:5000, where 5000 is default port)
# To change port: flask run --port=5001
# To run in debug mode: flask run --port=5001 --debug    (This is like --reload in FastApi, ie; on saving, it applies changes)

# Or include this at the base of the app.py page to enable run by clicking on the run command in the IDE. or via cmd command: python "python_filename.py"
'''
if __name__ == "__main__":
    app.run(debug=True)                               # Default
    app.run(host='0.0.0.0', port=8080)
'''

