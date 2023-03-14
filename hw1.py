from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hello world')

@dp.message_handler(commands=['mem'])
async def send_mem(message: types.Message):
    photo = open('cat.jpeg', 'rb')
    await message.answer_photo(photo=photo)

@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(text='button_1')
async def quiz_2(call: types.CallbackQuery):
    question = 'Что из приведенного является изменяемым типом данных?'
    answer = [
        'Строки',
        'Списки',
        'Кортежи',
        'Числа'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Стыдно не знать',
        open_period=5,

    )

@dp.message_handler()
async def echo(message: types.Message):
    try:
        number = float(message.text)
        result = number ** 2
        await message.answer(result)
    except ValueError:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)