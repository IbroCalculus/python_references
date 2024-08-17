from typing import Optional
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    secret_name: str = Field(max_length=100, nullable=False)
    age: Optional[int] = Field(default=None)
