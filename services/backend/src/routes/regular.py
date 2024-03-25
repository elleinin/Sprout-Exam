from typing import List
from http.client import responses
from urllib import response
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from tortoise.exceptions import DoesNotExist
from tortoise.contrib.fastapi import HTTPNotFoundError

import src.store.regular as store
from src.schemas.regulars import RegularSchema, UpdateRegularEmp

router = APIRouter()

@router.get("/regular")
async def get_all():
    return await store.get_all()

@router.get("/regular/{id}")
async def get_employee(id):
    return await store.get_employee(id)

@router.patch("/regular/{id}", response_model=RegularSchema)
async def update_employee(id: int, data: UpdateRegularEmp) -> RegularSchema:
    return await store.update_regular_emp(id, data)
