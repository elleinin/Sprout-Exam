from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "contractual" ALTER COLUMN "contract_end_date" TYPE VARCHAR(50) USING "contract_end_date"::VARCHAR(50);
        ALTER TABLE "contractual" ALTER COLUMN "contract_end_date" TYPE VARCHAR(50) USING "contract_end_date"::VARCHAR(50);
        ALTER TABLE "contractual" ALTER COLUMN "contract_end_date" TYPE VARCHAR(50) USING "contract_end_date"::VARCHAR(50);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "contractual" ALTER COLUMN "contract_end_date" TYPE DATE USING "contract_end_date"::DATE;
        ALTER TABLE "contractual" ALTER COLUMN "contract_end_date" TYPE DATE USING "contract_end_date"::DATE;
        ALTER TABLE "contractual" ALTER COLUMN "contract_end_date" TYPE DATE USING "contract_end_date"::DATE;"""
