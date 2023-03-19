from decouple import config

import string
import random


class Settings:
    DEBUG = config("DEBUG", cast=bool, default=False)

    DB_URL = "sqlite:///database.db"

    SECRET_KEY = config(
        "SECRET_KEY",
        default="".join([random.choice(string.ascii_letters) for _ in range(32)]),
    )


settings = Settings()
