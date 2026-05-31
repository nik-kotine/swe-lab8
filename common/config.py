from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

def require_env_variable(name) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"missing environment variable: {name}")
    if value.strip() == "":
        raise RuntimeError(f"empty environment variable: {name}")
    return value

RABBITMQ_HOST = require_env_variable("RABBITMQ_HOST")
RABBITMQ_PORT = require_env_variable("RABBITMQ_PORT")
RABBITMQ_USER = require_env_variable("RABBITMQ_USER")
RABBITMQ_PASSWORD = require_env_variable("RABBITMQ_PASSWORD")
RABBITMQ_VHOST = require_env_variable("RABBITMQ_VHOST")
RABBITMQ_QUEUE = require_env_variable("RABBITMQ_QUEUE")
REWARDS_DB = require_env_variable("REWARDS_DB")
SONAR_TOKEN = require_env_variable("SONAR_TOKEN")
