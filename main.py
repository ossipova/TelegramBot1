from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

       # QUESTION 1
@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)
    question = "What's the name of package-management in Python?"
    answer = [
        'random',
        'randin',
        'python-decouple',
        'pip',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='You should study better!',
        open_period=20,
        reply_markup=markup
    )

         # QUESTION 2
@dp.callback_query_handler(text='button_call_1')
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
@dp.callback_query_handler(text='button_call_2')
async def quiz_3(call: types.CallbackQuery):
    # markup = InlineKeyboardMarkup()
    # button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    # markup.add(button_call_2)
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
        # reply_markup=markup
    )

@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo = open('media/IMG_4316.JPG', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f'Hi! {message.from_user.first_name}')


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text)**2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
