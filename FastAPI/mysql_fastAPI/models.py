# This is used by the sqlalchemy uses to be able to create the tables needed in mysql database

from sqlalchemy import Boolean, Column, Integer, String
from database_conn import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)      #index=True implies it will improve mysql performance when search by id
    username = Column(String(50), unique=True)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)
