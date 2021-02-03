from typing import Optional
from telebot.types import Update
from fastapi import FastAPI, Request, Response, status

from bot.async_telebot import bot
from settings import WEBHOOK_URL_PATH


app = FastAPI()


@app.on_event('startup')
def startup():
  pass


@app.on_event('shutdown')
def shutdown():
  pass


@app.get('/')
async def index():
  return 'API'


@app.get(WEBHOOK_URL_PATH)
async def webhook(request: Request):
  if request.headers['content-type'] == 'application/json':
    json_string = await request.json()
    update = Update.de_json(json_string)
    bot.process_new_updates([update])
    return ''
  else:
    return Response(status_code=status.HTTP_403_FORBIDDEN)
