import profile
from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError


from src.database.models import Employee, Regular, Contractual
from src.schemas.employees import EmployeeSchema, ProfileSchema
from src.schemas.regulars import RegularEmpSchema, UpdateRegularEmp
from src.schemas.contractuals import ContractualSchema, UpdateContractualEmp


# universal functions

async def create_user(user) -> ProfileSchema:
    user_obj = user.dict(exclude_unset=True)
    profile = await Employee.create(**user_obj)
    if user_obj["employee_type"] == "Regular":
        await Regular.create(**user_obj)
    elif user_obj["employee_type"] == "Contractual":
        await Contractual.create(**user_obj)
    return await ProfileSchema.from_tortoise_orm(profile)

async def delete_user(user_id):
    try:
        await ProfileSchema.from_queryset_single(Employee.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

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

# async def update_employees():
#     regulars = await Regular.filter().values_list()
#     contractuals = await Contractual.filter().values_list()
#     return (regulars + contractuals)

async def get_count() -> int:
    user_count = await get_all()
    return len(user_count)

async def get_all():
    return await Employee.filter().values_list()

# regular employee functions

async def get_all_regular_emp():
    return await Regular.filter().values_list()

async def get_regular_emp(user_id) -> RegularEmpSchema:
    try:
        user = await RegularEmpSchema.from_queryset_single(Regular.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user

async def update_regular_emp(user_id: int, data: UpdateRegularEmp):
    try:
        await RegularEmpSchema.from_queryset_single(Regular.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    updated_count = await Regular.filter(id=user_id).update(**data.dict(exclude_unset=True))
    if not updated_count:
        raise HTTPException(status_code=400, detail=f"Error updating user {user_id}")
    return await RegularEmpSchema.from_queryset_single(Regular.get(id=user_id))

# contractual employee functions

async def get_all_contractual_emp():
    return await Contractual.filter().values_list()

async def get_contractual_emp(user_id) -> ContractualSchema:
    try:
        user = await ContractualSchema.from_queryset_single(Contractual.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user

async def update_contractual_emp(user_id: int, data: UpdateContractualEmp):
    try:
        await ContractualSchema.from_queryset_single(Contractual.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    updated_count = await Contractual.filter(id=user_id).update(**data.dict(exclude_unset=True))
    if not updated_count:
        raise HTTPException(status_code=400, detail=f"Error updating user {user_id}")
    return await ContractualSchema.from_queryset_single(Contractual.get(id=user_id))