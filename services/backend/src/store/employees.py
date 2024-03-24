from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError


from src.database.models import Employee
from src.schemas.employees import UserOutSchema, UserDatabaseSchema


async def create_user(user) -> UserOutSchema:
    user_obj = await Employee.create(**user.dict(exclude_unset=True))
    return await UserOutSchema.from_tortoise_orm(user_obj)

async def delete_user(user_id):
    try:
        await UserOutSchema.from_queryset_single(Employee.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    deleted_count = await Employee.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return f"Deleted user {user_id}"

async def get_user(user_id) -> UserDatabaseSchema:
    try:
        user = await UserDatabaseSchema.from_queryset_single(Employee.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user

async def get_all():
    return await Employee.filter().values_list()

async def get_count() -> int:
    user_count = await Employee.filter().values_list()
    return len(user_count)