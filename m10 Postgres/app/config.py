from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    # Field names MUST match the variable names in .env
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(
        env_file="./.env",          # relative to where you start the server
        env_ignore_empty=True,      # ignore empty values
        extra="ignore",             # ignore unrelated variables
    )

    @property
    def POSTGRES_URL(self) -> str:
        # postgresql + asyncpg driver  (pip install asyncpg)
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


# create ONE instance and import it wherever you need settings
settings = DatabaseSettings()
