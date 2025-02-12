from dotenv import dotenv_values
from aiogram import Bot, Dispatcher

config = dotenv_values(".env")

bot = Bot(config.get("TOKEN"))
dp = Dispatcher(bot)
