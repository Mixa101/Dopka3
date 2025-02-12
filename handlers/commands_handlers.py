from aiogram import types, Dispatcher
names = ['Islam', 'Zhanat', 'Bektur', 'Aziret', 'Roma', 'Eldos']
import random

# async def start_handler(message: types.Message):
#     await message.answer(f"Hello {message.from_user.username}!")

async def info_handler(message: types.Message):
    await message.answer(f"ваш ID: {message.from_user.id}\n"
                         f"ваше имя: {message.from_user.first_name}\n"
                         f"ваше никнейм: {message.from_user.username}")

async def send_random(message: types.Message):
    name = random.choice(names)
    await message.answer(f"Случайное имя из списка: {name}")

def register_commands_handlers(dp : Dispatcher):
    # dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(info_handler, commands=["myinfo"])
    dp.register_message_handler(send_random, commands=["random"])