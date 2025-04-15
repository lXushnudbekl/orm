from tortoise import Tortoise
from config import get_settings

settings = get_settings()

DB_URL = f'postgres://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}'
DATABASE_URL = settings.database_url

DB_CONFIG = {
    "connections": {
        "default": f"{DB_URL}"
    },
    "apps": {
        "models": {
            "models": ["models.user", "models.book", "aerich.models"],
            "default_connection": "default",
        }
    }
}


async def init_db():
    await Tortoise.init(config=DB_CONFIG)
