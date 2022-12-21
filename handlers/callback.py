from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp
from config import Dispatcher


# QUESTION 2
# @dp.callback_query_handler(text='button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_2)
    question = "What's the name of framework for creating Telegram Bot?"
    answer = [
        'aiogram',
        'executor',
        'bot',
        'token',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='You should study better!',
        open_period=20,
        reply_markup=markup
    )




   # QUESTION 3
# @dp.callback_query_handler(text='button_call_2')
async def quiz_3(call: types.CallbackQuery):
    question = "What command outputs all moduls and packages of your project to a text file?"
    answer = [
        'pip freezeng -> requirements.txt',
        'pip freeze -> req.txt',
        'pip install requirements.txt',
        'python freeze req.txt',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='You should study better!',
        open_period=20,
    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
    dp.register_callback_query_handler(quiz_3, text='button_call_2')
