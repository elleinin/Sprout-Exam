from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "employee" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50),
    "last_name" VARCHAR(50),
    "email" VARCHAR(50),
    "employee_type" VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "contractual" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "contract_end_date" VARCHAR(50),
    "project" TEXT,
    "employee_id_id" INT NOT NULL REFERENCES "employee" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "regular" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "number_of_leaves" DOUBLE PRECISION,
    "benefits" JSONB,
    "employee_id_id" INT NOT NULL REFERENCES "employee" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
