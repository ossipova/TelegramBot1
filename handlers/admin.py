from aiogram import types, Dispatcher
from config import bot, ADMINS
from database.bot_db import sql_command_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('You are not an admin!')
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(f'{user[0]}, {user[1]}, {user[2]}, {user[3]}, {user[4]}',
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
                                     f'delete{user[1]}', callback_data=f'delete {user[0]}')))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])
