from typing import Optional
from unicodedata import name

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Contractual

ContractualInSchema = pydantic_model_creator(
    Contractual, name="RegularIn", exclude_readonly=True
)
ContractualOutSchema = pydantic_model_creator(
    Contractual, name="RegularOut"
)

class UpdateContractualEmployee(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email = Optional[str]