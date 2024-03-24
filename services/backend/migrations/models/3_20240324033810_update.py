from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "contractual" ADD "employee_type" VARCHAR(50) NOT NULL;
        ALTER TABLE "employee" ADD "employee_type" VARCHAR(50) NOT NULL;
        ALTER TABLE "regular" ADD "employee_type" VARCHAR(50) NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "regular" DROP COLUMN "employee_type";
        ALTER TABLE "employee" DROP COLUMN "employee_type";
        ALTER TABLE "contractual" DROP COLUMN "employee_type";"""
