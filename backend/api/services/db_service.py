from contextlib import asynccontextmanager

from models.db_helper import db_helper

@asynccontextmanager
async def lifespan(app):
    # startup database
    yield
    # shutdown database
    print("Shutting down database...")
    await db_helper.dispose()