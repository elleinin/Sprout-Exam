from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

from src.routes import employees
from src.routes import regular
from src.routes import contractual
import src.store.employees as store

app = FastAPI()

# connection to frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router)
app.include_router(regular.router)
app.include_router(contractual.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "count!"
