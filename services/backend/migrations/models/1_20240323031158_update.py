from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "contractual" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50),
    "last_name" VARCHAR(50),
    "email" VARCHAR(50),
    "contract_end_date" DATE,
    "benefits" DATE
);;
        CREATE TABLE IF NOT EXISTS "regular" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50),
    "last_name" VARCHAR(50),
    "email" VARCHAR(50),
    "number_of_leaves" DOUBLE PRECISION,
    "benefits" JSONB
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "contractual";
        DROP TABLE IF EXISTS "regular";"""
