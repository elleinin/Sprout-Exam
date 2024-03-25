import profile
from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Regular
from src.schemas.regulars import RegularSchema, UpdateRegularEmp

async def get_all():
    return await Regular.filter().values_list()

async def get_employee(employee_id) -> RegularSchema:
    try:
        user = await RegularSchema.from_queryset_single(Regular.get(employee_id=employee_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")
    return user

async def update_employee(employee_id: int, data: UpdateRegularEmp):
    try:
        await RegularSchema.from_queryset_single(Regular.get(employee_id=employee_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")

    updated_count = await Regular.filter(employee_id=employee_id).update(**data.dict(exclude_unset=True))
    if not updated_count:
        raise HTTPException(status_code=400, detail=f"Error updating user {employee_id}")
    return await RegularSchema.from_queryset_single(Regular.get(employee_id=employee_id))

async def delete_employee(employee_id):
    try:
        await RegularSchema.from_queryset_single(Regular.get(employee_id=employee_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")

    deleted_count = await Regular.filter(employee_id=employee_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {employee_id} not found")
    return f"Deleted user {employee_id}"