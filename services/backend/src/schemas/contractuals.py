from typing import Optional, List
from unicodedata import name

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Contractual

ContractualSchema = pydantic_model_creator(
    Contractual, name="Contractual"
)

class UpdateContractualEmp(BaseModel):
    contract_end_date: Optional[str]
    benefits: Optional[List]