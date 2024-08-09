from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# pip install aiofiles

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Accessing static files'}


# NB: Want to be able to access the file, ie
app.mount('/some_files', StaticFiles(directory='some_files'), name='some_files')        # localhost:8000/some_files/lambo1.jpeg

# Mounting the static files directory
# Path: /static_files (URL path to access the files)
# Directory: files_directory (actual directory on the filesystem)
# Name: static_files_mount (internal name for the mount)
# app.mount('/static_files', StaticFiles(directory='files_directory'), name='static_files_mount')     # http://localhost:8000/static_files/lambo1.jpeg