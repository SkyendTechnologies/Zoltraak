from pydantic import (
    BaseModel,
    PostgresDsn,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)

# Config run settings
class RunSettings(BaseModel):
    host: str = "localhost"
    port: int = 8000

# Config api prefix
class ApiPrefixSettings(BaseModel):
    v1: str = "/api/v1"
    v2: str = "/api/v2"

# Config database in postgres
class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

# Config base settings api
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="API_ZOL__"
    )
    run: RunSettings = RunSettings()
    api_prefix: ApiPrefixSettings = ApiPrefixSettings(
        v1="/api/v1",
        v2="/api/v2"
    )
    db: DatabaseConfig


settings = Settings()