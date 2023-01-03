from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp
from database.bot_db import sql_command_random
from parser.news import ParserNews


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f'Hi! {message.from_user.first_name}')


# QUESTION 1
# @dp.message_handler(commands=['quiz'])
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


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo = open('media/IMG_4316.JPG', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


# @dp.message_handler(commands=['pin'])
async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('What to pin?')


async def get_random_user(message: types.Message):
    await sql_command_random(message)


async def get_news(message: types.Message):
    news = ParserNews.parser()
    for i in news:
        await message.answer(
            f"{i['link']}\n\n"
            f"{i['title']}\n"
            f"{i['dop']}\n"
            f"#t{i['time']}\n"
            f"#d{i['date']}\n"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_news, commands=['news'])
