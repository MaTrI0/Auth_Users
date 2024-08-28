from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self):
        self.SQLALCHEMY_URL = "postgresql+psycopg2://postgres:root@localhost/fastapi_AuthUsers"

        self.engine = create_engine(self.SQLALCHEMY_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

database = Database()
