from tortoise.contrib.pydantic import pydantic_model_creator


from src.database.models import Admin


AdminSchema = pydantic_model_creator(
    Admin, name="Login", exclude_readonly=True
)