from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError


from src.database.models import Employee, Regular, Contractual, Admin
from src.store.regular import delete_employee as delete_regular
from src.store.contractual import delete_employee as delete_contractual
from src.schemas.employees import EmployeeSchema, ProfileSchema
from src.schemas.users import AdminSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# universal user functions

async def create_user(user, type) -> EmployeeSchema:
    user_obj = user.dict(exclude_unset=True)
    profile = await Employee.create(**user_obj) # create employee profile entry
    # id_count = await get_id_count()
    # last = await Employee.get(id=id_count)
    # print(last)
    data = {"profile": profile}
    if type == "Regular":
        await Regular.create(**data)
    elif type == "Contractual":
        await Contractual.create(**data)
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

async def get_all():
    return await Employee.filter().values()

async def get_id_count():
    list = await get_all()
    count = len(list)
    print(count)
    if count > 0:
        return count
    else:
        return 0

async def wipe(): # for testing
    await Employee.filter().delete()
    await Regular.filter().delete()
    await Contractual.filter().delete()
    return f"Deleted"

# ADMIN USER

async def create_admin(user) -> AdminSchema:
    try:
        user_obj = await Admin.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(status_code=401, detail=f"Sorry, that username already exists.")

    return await AdminSchema.from_tortoise_orm(user_obj)

async def login_admin(user: AdminSchema):
    admin = await Admin.filter(username=user.username, password=user.password)
    return admin

async def delete_admins():
    await Admin.filter().delete()
    return f"Deleted"
