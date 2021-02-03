import os
from dotenv import load_dotenv


# Dotenv loading
# Dotenv https://pypi.org/project/python-dotenv/
load_dotenv(dotenv_path="../.env")


# Uvicorn serrings
# Uvicorn https://www.uvicorn.org/
PORT: int = int(os.environ.get('PORT', '80'))
LOG_LEVEL: str = 'debug'


# Bot settings
# Telebot https://pypi.org/project/pyTelegramBotAPI/
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

WEBHOOK_HOST = os.environ.get('WEBHOOK_HOST')
WEBHOOK_PORT = os.environ.get('WEBHOOK_PORT')

WEBHOOK_SSL_CERT = './'
WEBHOOK_SSL_PRIV = './'

WEBHOOK_URL_PATH = f'/{BOT_TOKEN}/'

# Redis as broker
# Redis https://redis.io/
TASKS_REDIS = {
    'HOST': os.environ.get('TASKS_REDIS_HOST', 'tasks'),
    'PORT': os.environ.get('TASKS_REDIS_PORT', '6379')
}


# Redis as database
# Redis https://redis.io/
GAMES_REDIS = {
    'HOST': os.environ.get('GAMES_REDIS_HOST', 'games'),
    'PORT': os.environ.get('GAMES_REDIS_PORT', '6379')
}
