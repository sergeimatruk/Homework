from aiogram import types, Dispatcher
from config import ADMINS

async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не админ')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban)