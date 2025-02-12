from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard = True)
    keyboard.add(InlineKeyboardButton(text="контакты", callback_data="contacts"), InlineKeyboardButton(text="Наш адресс", callback_data="adress"),
                 InlineKeyboardButton(text="наш сайт", callback_data="site"), InlineKeyboardButton(text="Меню", callback_data="menu"))
    
    await message.answer("Добро пожаловать в нашу пиццерию!", reply_markup=keyboard)


def register_pizza_handler(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])