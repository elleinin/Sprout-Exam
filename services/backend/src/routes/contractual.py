from typing import List
from http.client import responses
from urllib import response
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from tortoise.exceptions import DoesNotExist
from tortoise.contrib.fastapi import HTTPNotFoundError

import src.store.employees as store
from src.schemas.contractuals import ContractualSchema, UpdateContractualEmp

router = APIRouter()

@router.get("/contractual")
async def get_all():
    return await store.get_all_contractual_emp()

@router.get("/contractual/{id}")
async def get_employee(id):
    return await store.get_contractual_emp(id)

@router.patch("/contractual/{id}", response_model=ContractualSchema)
async def update_employee(id: int, data: UpdateContractualEmp) -> ContractualSchema:
    return await store.update_contractual_emp(id, data)
