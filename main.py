from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from db import engine, Base
import models
from routes import user_routes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)
