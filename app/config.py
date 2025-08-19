#psydantic is used for type validation. eg: it validates data before entering into database.
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

#    class ConfigDict:
#        env_file = ".env"

settings = Settings()