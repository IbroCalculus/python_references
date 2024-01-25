import datetime

from pydantic import BaseModel, validator, field_validator
from typing import Optional
from enum import Enum


class User(BaseModel):
    id: int
    full_name: str = "Default name"
    age: Optional[int] = 18


person1 = User(id=1, full_name="Jane Doe")
print(person1)
print(person1.full_name)


# ==========================================================
class Level(int, Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    date_joined: datetime.date
    level: Level

    @field_validator("age")
    def check_age(cls, age, values):
        if age < 0 or age > 120:
            print("Age must be between 0 and 120.")
            return
        print(f"Age is {age}, while...\nValues are: {values}")
        return age                  # If not return, then it will be; age = None


student1 = Student(
    first_name="Student1",
    last_name="One",
    age=23,
    date_joined=datetime.date(2014, 5, 21),
    level=Level.BEGINNER
)
# print(student1)
