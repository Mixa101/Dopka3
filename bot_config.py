from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


config = dotenv_values(".env")

bot = Bot(config.get("TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())
