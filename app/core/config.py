from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    MT5_SERVER = os.getenv("MT5_SERVER")
    MT5_LOGIN = int(os.getenv("MT5_LOGIN"))
    MT5_PASSWORD = os.getenv("MT5_PASSWORD")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT"))

settings = Settings()
