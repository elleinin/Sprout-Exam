from typing import Optional, List
from unicodedata import name

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Regular

RegularSchema = pydantic_model_creator(
    Regular, name="RegularEmployee"
)

class UpdateRegularEmp(BaseModel):
    number_of_leaves: Optional[float]
    benefits: Optional[List]