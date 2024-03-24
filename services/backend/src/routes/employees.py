from typing import List
from http.client import responses
from urllib import response
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from tortoise.exceptions import DoesNotExist
from tortoise.contrib.fastapi import HTTPNotFoundError

import src.store.employees as store
from src.schemas.employees import UserInSchema, UserOutSchema, UserDatabaseSchema


router = APIRouter()

@router.post("/register", response_model=UserOutSchema)
async def create_user(user: UserDatabaseSchema) -> UserOutSchema:
    return await store.create_user(user)

@router.get("/employees")
async def get_all():
    return await store.get_all()

@router.get("/count")
async def get_count():
    return await store.get_count()

@router.get("/employee/{id}", response_model=UserDatabaseSchema)
async def get_user(id: int) -> UserDatabaseSchema:
    try:
        return await store.get_user(id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist",
        )

@router.delete(
    "/employee/{id}",
    responses={
        400: {"model": HTTPNotFoundError}
    },
)
async def delete_user(id: int):
    return await store.delete_user(id)
