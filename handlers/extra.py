from aiogram import types
from config import bot, Dispatcher
import random

# @dp.message_handler()
async def echo(message: types.Message):
    try:
        number = float(message.text)
        result = number ** 2
        await message.answer(result)
    except ValueError:
        await bot.send_message(message.from_user.id, message.text)

    if message.text.startswith('!pin'):
        if message.reply_to_message is not None:
            await message.pin()


    if message.text.startswith('game'):
        emojis = ['🎯', '🎳', '⚽️', '🏀', '🎰', '🎲']
        emoji = random.choice(emojis)
        await message.answer(emoji)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)