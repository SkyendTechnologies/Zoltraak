from typing import AsyncGenerator

import logging
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker
)
from config import Settings


settings = Settings


async def get_settings():
    db_listing = [
        settings.db.url,
        settings.db.echo,
        settings.db.echo_pool,
        settings.db.pool_size,
        settings.db.max_overflow
    ]

    return db_listing

class DatabaseHelper:
    def __init__(
        self,
        database_url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 0
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=database_url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow
        )

        self.session: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def dispose(self) -> None:
        """Closes the connection to the database."""
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Provides a session for database operations."""
        async with self.session() as session:
            yield session


# Initialize the database helper
try:
    print("Setting up database...")
    db_helper = DatabaseHelper(
        database_url = "postgresql+asyncpg://root:toor@localhost:5432/zoltraakAPI",
        echo = False,
        echo_pool = False,
        pool_size = 50,
        max_overflow = 10
    )

    print("Database setup complete.")
except AttributeError as e:
    print("Error during initialization:", e)
    print("Ensure that the 'db' section is properly defined in your settings.")
    raise
