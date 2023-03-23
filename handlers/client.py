from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, Dispatcher
from database.bot_db import sql_command_random

# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hello world')

# @dp.message_handler(commands=['mem'])
async def send_mem(message: types.Message):
    photo = open('cat.jpeg', 'rb')
    await message.answer_photo(photo=photo)

# @dp.message_handler(commands=['quiz'])
async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('NEXT', callback_data='button_1')
    markup.add(button_1)
    question = 'Какая типизация используется в Python?'
    answer = [
        'Статистическая',
        'Последовательная',
        'Динамическая'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Стыдно не знать',
        open_period=5,
        reply_markup=markup

    )

async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer(
        caption=f"{random_user[0]} {random_user[1]} {random_user[2]} {random_user[3]}\n"
                f"@{random_user[4]}"
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(send_mem, commands=['mem'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])