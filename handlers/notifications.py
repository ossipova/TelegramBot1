import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('Ok!')


async def time_to_pay():
    await bot.send_message(chat_id=chat_id, text="It's time to pay your bills!")


async def renew_membership():
    await bot.send_message(chat_id=chat_id, text="It's time to renew your membership!")


async def scheduler():
    aioschedule.every().monday.at('10:00').do(time_to_pay)
    aioschedule.every().saturday.at('13:00').do(renew_membership)


    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'remind' in word.text)
