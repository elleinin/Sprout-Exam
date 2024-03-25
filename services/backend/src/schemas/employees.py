from typing import Optional
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator


from src.database.models import Employee


EmployeeSchema = pydantic_model_creator(
    Employee, name="UserIn", exclude_readonly=True
)
ProfileSchema = pydantic_model_creator(
    Employee, name="UserOut", exclude=["id"]
)

class UpdateEmployee(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email = Optional[str]