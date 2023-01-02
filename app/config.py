from pydantic import BaseSettings

PEOPLE_API_SUFFIX = '/api/people'
HEALTHCHECKER_API_SUFFIX = '/api/healthchecker'
API_TOKEN = "TEST-API-TOKEN"


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = './.env'


settings = Settings()