from starlette.config import Config
from starlette.datastructures import Secret


try:
    config = Config(".env")
except:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)

connection_string = str(DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
