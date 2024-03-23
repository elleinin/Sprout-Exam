from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Employee


UserInSchema = pydantic_model_creator(
    Employee, name="UserIn", exclude_readonly=True
)
UserOutSchema = pydantic_model_creator(
    Employee, name="UserOut", exclude=["id","email"]
)
UserDatabaseSchema = pydantic_model_creator(
    Employee, name="User"
)