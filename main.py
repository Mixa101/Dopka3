from aiogram import executor
from dotenv import dotenv_values
from handlers import commands_handlers, start_commands, review_dialog
from bot_config import dp
import logging

commands_handlers.register_commands_handlers(dp)
start_commands.register_pizza_handler(dp)
review_dialog.register_review_handler(dp)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, allowed_updates=["callback"])