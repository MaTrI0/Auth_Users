from sqlalchemy import Boolean, Column, Integer, String
from ..database import database

class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))
