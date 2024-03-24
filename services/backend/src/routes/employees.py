from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from tortoise.contrib.fastapi import HTTPNotFoundError

import src.store.employees as crud
from src.schemas.employees import UserInSchema, UserOutSchema

router = APIRouter()

@router.post("/register", response_model=UserOutSchema)
async def create_user(user: UserInSchema) -> UserOutSchema:
    return await crud.create_user(user)