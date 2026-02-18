from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import engine, Base
import models
from routes import user_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
