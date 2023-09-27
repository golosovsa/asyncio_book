import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_DIR / 'secrets.env')


def get_secret(key: str) -> str:
    return os.getenv(key)
