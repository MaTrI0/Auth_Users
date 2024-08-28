from pydantic import BaseModel

class SUser(BaseModel):
    id: int
    user_id: int
    username: str
    password: str
    email: str

class SUserID(BaseModel):
    user_id: int

class SUserUpdate(BaseModel):
    username: str
    password: str
    email: str
