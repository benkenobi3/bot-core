from telebot import AsyncTeleBot
from settings import BOT_TOKEN


bot = AsyncTeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
async def add(message):
    bot.send_message(message.chat.id, "nice")
