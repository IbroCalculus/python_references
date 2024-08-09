from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastAPI.sql_alchemy import db_user
from fastAPI.sql_alchemy.db.database_conn import get_db
from fastAPI.sql_alchemy.schemas import UserBase

router = APIRouter(prefix='/user', tags=['user'])

# CREATE
@router.create('/')
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# READ


# UPDATE


# DELETE