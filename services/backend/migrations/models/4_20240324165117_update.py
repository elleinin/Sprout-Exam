from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "contractual" DROP COLUMN "contract_end_date";
        ALTER TABLE "contractual" DROP COLUMN "benefits";
        ALTER TABLE "regular" DROP COLUMN "number_of_leaves";
        ALTER TABLE "regular" DROP COLUMN "benefits";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "regular" ADD "number_of_leaves" DOUBLE PRECISION;
        ALTER TABLE "regular" ADD "benefits" JSONB;
        ALTER TABLE "contractual" ADD "contract_end_date" DATE;
        ALTER TABLE "contractual" ADD "benefits" JSONB;"""
