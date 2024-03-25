from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.exceptions import DoesNotExist
from tortoise.contrib.fastapi import HTTPNotFoundError

import src.store.employees as store
from src.schemas.employees import EmployeeSchema
from src.schemas.users import AdminSchema
from src.auth.admin import validate_user

from src.auth.jwthandler import (
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

router = APIRouter()

# Universal user routes

@router.post("/employee", response_model=EmployeeSchema)
async def create_user(user:EmployeeSchema, type) -> EmployeeSchema:
    return await store.create_user(user, type)

@router.delete(
    "/employee/{id}",
    responses={
        400: {"model": HTTPNotFoundError}
    },
)
async def delete_user(id: int, type):
    return await store.delete_user(id, type)

@router.get("/employee/{id}", response_model=EmployeeSchema)
async def get_user(id: int) -> EmployeeSchema:
    try:
        return await store.get_user(id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist",
        )

@router.get("/employees")
async def get_all():
    return await store.get_all()

# @router.get("/count") # for testing
# async def get_count():
#     return await store.get_count()

@router.delete("/wipe")
async def wipe():
    return await store.wipe()

# ADMIN USER

@router.post("/register", response_model=AdminSchema)
async def create_user(user: AdminSchema) -> AdminSchema:
    return await store.create_adminr(user)


@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response