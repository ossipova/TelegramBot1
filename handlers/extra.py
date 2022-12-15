from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)
    elif message.text.startswith('game') and message.from_user.id in ADMINS:
        data = ['🎲', '🎯', '🎰', '🎳', '🏀', '⚽']
        r = random.choice(data)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
