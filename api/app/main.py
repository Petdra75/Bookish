from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import bookish

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bookish.router)