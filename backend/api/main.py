import logging
import os

from fastapi import FastAPI
import uvicorn
from logs import init_logger

from config import settings
from routers import Routering
from services.db_service import lifespan

# debug
init_logger(logging.DEBUG)

# Отладочный вывод
print(f"Type of settings: {type(settings)}")
print(f"settings.model_dump(): {settings.model_dump()}")

print(f"settings.api_prefix.v1: {settings.api_prefix.v1} ({type(settings.api_prefix.v1)})")
print(f"settings.api_prefix.v2: {settings.api_prefix.v2} ({type(settings.api_prefix.v2)})")
print(f"settings.run.host: {settings.run.host} ({type(settings.run.host)})")
print(f"settings.run.port: {settings.run.port} ({type(settings.run.port)})")

app = FastAPI(
    title="Zoltraak API",
    lifespan=lifespan
)
app.include_router(
    Routering(),
    prefix=settings.api_prefix.v1  # Префикс должен быть корректным
)

if __name__ == "__main__":
    print("Starting server...")

    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )

