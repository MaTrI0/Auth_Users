import uvicorn
from fastapi import FastAPI

from src.database import database
from src.routers.user import router as UserRouter


database.Base.metadata.create_all(bind=database.engine)
app = FastAPI(
    title="Auth user App"
)

app.include_router(UserRouter, prefix="/api/v1/users")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=3)
