from typing import Optional
from unicodedata import name

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Regular

RegularInSchema = pydantic_model_creator(
    Regular, name="RegularIn", exclude_readonly=True
)
RegularOutSchema = pydantic_model_creator(
    Regular, name="RegularOut"
)