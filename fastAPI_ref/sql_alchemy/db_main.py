from fastapi import FastAPI

from db import models
from db.database_conn import engine

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello, World!"}


models.Base.metadata.create_all(bind=engine)
