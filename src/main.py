import time
import uvicorn
from bot.async_telebot import bot
from settings import PORT, LOG_LEVEL, WEBHOOK_URL


if __name__ == '__main__':
    bot.remove_webhook()

    time.sleep(0.1)

    # Without certs
    bot.set_webhook(url=WEBHOOK_URL)

    uvicorn.run('app.fastapi:app', host="0.0.0.0", port=PORT, log_level=LOG_LEVEL, reload=True)
