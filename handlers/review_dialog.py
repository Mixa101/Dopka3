from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

class PizzeriaReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()
    

async def start_review(call: types.CallbackQuery):
    await call.message.answer("Введите ваше имя: ")
    await PizzeriaReview.name.set()

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.answer("Введите ваш номер телефона:")
    await PizzeriaReview.next()

async def load_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text
    await message.answer("Введите рейтинг:")
    await PizzeriaReview.next()

async def load_rate(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rate'] = message.text
    await message.answer("Введите дополнительные комментарии/жалобы")
    await PizzeriaReview.next()

async def load_extra_comments(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['extra_comments'] = message.text
        
        await message.answer(f"Ваш отзыв: \n"
                             f"имя: {data['name']}\n"
                             f"номер телефона: {data['phone_number']}\n"
                             f"отзыв: {data['rate']}\n"
                             f"доп комменты: {data['extra_comments']}")

def register_review_handler(dp : Dispatcher):
    dp.register_callback_query_handler(start_review, Text(equals="review"))
    dp.register_message_handler(load_name, state=PizzeriaReview.name)
    dp.register_message_handler(load_phone_number, state=PizzeriaReview.phone_number)
    dp.register_message_handler(load_rate, state=PizzeriaReview.rate)
    dp.register_message_handler(load_extra_comments, state=PizzeriaReview.extra_comments)