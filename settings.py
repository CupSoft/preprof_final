from decouple import config

import string
import random


class Settings:
    DEBUG = config("DEBUG", cast=bool, default=False)

    DB_URL = "sqlite:///database.db"

    OXYGYN_PRICE = config("OXYGYN_PRICE", cast=int, default=7)
    FUEL_PRICE = config("FUEL_PRICE", cast=int, default=10)

    SECRET_KEY = config(
        "SECRET_KEY",
        default="".join([random.choice(string.ascii_letters) for _ in range(32)]),
    )


settings = Settings()
