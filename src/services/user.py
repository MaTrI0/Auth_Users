from ..models.user import User
from sqlalchemy.orm import Session
from ..dto.user import SUser, SUserUpdate

class UserService:
    def create_user(self, data: SUser, db: Session):
        user = User(user_id=data.user_id, username=data.username, email=data.email, password=data.password)

        try:
            db.add(user)
            db.commit()
            db.refresh(user)
        except Exception as e:
            print(e)

        return user

    def get_user(self, user_id: int, db: Session):
        return db.query(User).filter(User.user_id == user_id).first()

    def update(self, user_id: int, data: SUserUpdate, db: Session):
        user = db.query(User).filter(User.user_id == user_id).first()

        user.username = data.username
        user.email = data.email
        user.password = data.password

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def remove(self, user_id: int, db: Session):
        user = db.query(User).filter(User.user_id == user_id).delete()
        db.commit()
