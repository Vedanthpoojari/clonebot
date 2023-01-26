#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1997614911:AAGKVn8tLE4qRLDZiPIMo07TRy0VNEeNsrE")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "5938966"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "452a743cfbae846f25f48fb7d5ecdef4")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
