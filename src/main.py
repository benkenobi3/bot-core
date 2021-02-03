import time
import uvicorn
from bot.async_telebot import bot
from settings import PORT, LOG_LEVEL, WEBHOOK_URL_PATH


if __name__ == '__main__':
    bot.remove_webhook()

    time.sleep(0.1)

    bot.set_webhook(url='', certificate=open(WEBHOOK_SSL_CERT, 'r'))

    uvicorn.run('app.fastapi:app', host="0.0.0.0", port=PORT, log_level=LOG_LEVEL, reload=True)
