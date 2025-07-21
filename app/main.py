# main.py
from fastapi import FastAPI
from .database import engine, Base
from .api import bogie_checksheet, wheel_specifications

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    bogie_checksheet.router,
    prefix="/api/forms",
    tags=["bogie-checksheets"]
)

app.include_router(
    wheel_specifications.router,
    prefix="/api/forms",
    tags=["wheel-specifications"]
)