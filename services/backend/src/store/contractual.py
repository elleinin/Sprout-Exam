import profile
from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Contractual
from src.schemas.contractuals import ContractualSchema, UpdateContractualEmp

async def get_all():
    return await Contractual.filter().values_list()

async def get_employee(employee_id) -> ContractualSchema:
    try:
        user = await ContractualSchema.from_queryset_single(Contractual.get(employee_id=employee_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")
    return user

async def update_employee(employee_id: int, data: UpdateContractualEmp):
    try:
        await ContractualSchema.from_queryset_single(Contractual.get(employee_id=employee_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")

    updated_count = await Contractual.filter(employee_id=employee_id).update(**data.dict(exclude_unset=True))
    if not updated_count:
        raise HTTPException(status_code=400, detail=f"Error updating user {employee_id}")
    return await ContractualSchema.from_queryset_single(Contractual.get(employee_id=employee_id))

async def delete_employee(employee_id):
    try:
        await ContractualSchema.from_queryset_single(Contractual.get(employee_id=employee_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")

    deleted_count = await Contractual.filter(employee_id=employee_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")
    return f"Deleted user {employee_id}"