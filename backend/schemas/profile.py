# schemas/profile.py
from pydantic import BaseModel
from datetime import date

class ProfileUpdate(BaseModel):
    name: str
    date_of_birth: date
    gender: str
