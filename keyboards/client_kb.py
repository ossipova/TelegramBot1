from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True).add(KeyboardButton('yes'), KeyboardButton('no'))


cancel_marcup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True).add(KeyboardButton('Cancel'))
