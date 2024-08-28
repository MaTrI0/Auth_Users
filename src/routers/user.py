from typing import Annotated, List

from ..models.user import User
from ..database import database
from sqlalchemy.orm import Session
from ..services.user import UserService
from ..dto.user import SUser, SUserID, SUserUpdate
from fastapi import APIRouter, Depends

router = APIRouter(tags=["users"])


@router.post("/") # Add user in database
async def create_user(data: Annotated[SUser, Depends()] = None, db: Session = Depends(database.get_db)):
    user = UserService().create_user(data, db)
    return {"status": 200, "data": user}


@router.get("/{user_id}") # Get user by id
async def get_user_by_id(user_id: str = None, db: Session = Depends(database.get_db)):
    user = UserService().get_user(user_id, db)
    return {"status": 200, "data": user}


@router.put("/{user_id}")
async def update_user_by_id(user_id: str = None, data: Annotated[SUserUpdate, Depends()] = None, db: Session = Depends(database.get_db)):
    user = UserService().update(user_id, data, db)
    return {"status": 200, "data": user}


@router.delete("/{user_id}")
async def delete_user_by_id(user_id: str = None, db: Session = Depends(database.get_db)):
    UserService().remove(user_id, db)
    return {"status": 200}
