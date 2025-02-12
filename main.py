from aiogram import executor, Dispatcher, Bot, types
from dotenv import dotenv_values
import random
import logging

config = dotenv_values(".env")
names = ['Islam', 'Zhanat', 'Bektur', 'Aziret', 'Roma', 'Eldos']

bot = Bot(config.get("TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(f"Hello {message.from_user.username}!")

@dp.message_handler(commands=["myinfo"])
async def info_handler(message: types.Message):
    await message.answer(f"ваш ID: {message.from_user.id}\n"
                         f"ваше имя: {message.from_user.first_name}\n"
                         f"ваше никнейм: {message.from_user.username}")

@dp.message_handler(commands=["random"])
async def send_random(message: types.Message):
    name = random.choice(names)
    await message.answer(f"Случайное имя из списка: {name}")


if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)