from aiogram import types, Dispatcher
from config import ADMINS
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не админ')

async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не админ")
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(
                caption=f"{user[0]} {user[1]} {user[2]} {user[3]}\n"
                        f"@{user[4]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"DELETE {user[2]}",
                                         callback_data=f"DELETE {user[0]}")
                )
            )

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("DELETE ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await call.message.delete()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("DELETE "))