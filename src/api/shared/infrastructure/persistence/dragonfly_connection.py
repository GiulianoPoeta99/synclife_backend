import os

import redis
from dotenv import load_dotenv

load_dotenv()

PASS = os.getenv("DRAGONFLY_PASS")
HOST = os.getenv("DRAGONFLY_HOST")
PORT = os.getenv("DRAGONFLY_PORT")


DATABASE_URL: str = f"redis://:{PASS}@{HOST}:{PORT}"


def get_dragonfly_connection() -> redis.Redis:
    return redis.Redis.from_url(DATABASE_URL, decode_responses=True)
