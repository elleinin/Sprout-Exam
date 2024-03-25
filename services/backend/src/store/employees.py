import profile
from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError


from src.database.models import Employee, Regular, Contractual
from src.store.regular import delete_employee as delete_regular
from src.store.contractual import delete_employee as delete_contractual
from src.schemas.employees import EmployeeSchema, ProfileSchema

# universal user functions

async def create_user(user) -> EmployeeSchema:
    user_obj = user.dict(exclude_unset=True)
    profile = await Employee.create(**user_obj)
    if user_obj["employee_type"] == "Regular":
        await Regular.create()
    elif user_obj["employee_type"] == "Contractual":
        await Contractual.create()
    return await EmployeeSchema.from_tortoise_orm(profile)

async def delete_user(user_id, type):
    try:
        await ProfileSchema.from_queryset_single(Employee.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    if type == "Regular":
        await delete_regular(user_id)
    elif type == "Contractual":
        await delete_contractual(user_id)
    
    deleted_count = await Employee.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    return f"Deleted user {user_id}"

async def get_user(user_id) -> EmployeeSchema:
    try:
        user = await EmployeeSchema.from_queryset_single(Employee.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user

async def update_user(user, user_id):
    try:
        await ProfileSchema.from_queryset_single(Employee.get(user_id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    updated_count = await Employee.filter(employee_id=user_id).update(**user.dict(exclude_unset=True))
    if not updated_count:
        raise HTTPException(status_code=400, detail=f"Error updating user {user_id}")
    return await ProfileSchema.from_queryset_single(Employee.get(user_id=user_id))

# async def get_count() -> int: # for testing
#     user_count = await get_all()
#     return len(user_count)

async def get_all():
    return await Employee.filter().values_list()