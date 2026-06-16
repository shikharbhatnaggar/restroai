# config.py

import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SESSION_TIMEOUT = int(
    os.getenv("SESSION_TIMEOUT_MINUTES", 120)
)