from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import client_kb


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    age = State()
    course = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('What is your name?', reply_markup=client_kb.cancel_marcup)
    else:
        await message.answer('Write to private!')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['name'] = message.text
    await FSMAdmin.age.set()  # or .next()
    await message.answer('How old are you?')


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('The age format is not correct!')
    elif int(message.text) < 18:
        await message.answer('You must be 18 years old to visit this page!')
    elif int(message.text) > 100:
        await message.answer('Please input correct data!')
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('What is your course?')


async def load_course(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['course'] = message.text
    await FSMAdmin.next()
    await message.answer('What is your group?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"{data['name,']} {data['age,']} {data['course,']} {data['group']}")
    await FSMAdmin.next()
    await message.answer('Please check your answers,are they correct?', reply_markup=client_kb.submit_markup)


async def submit_fsm(message: types.Message, state: FSMContext):
    if message.text.lower() == 'yes':
        await state.finish()
        await message.answer('Thank you!')
    elif message.text.lower() == 'no':
        await state.finish()
        await message.answer('The registration is cancel!')
    else:
        await message.answer('The end!')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Ok, next time!')


def register_handlers_fsm_admin_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_course, state=FSMAdmin.course)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit_fsm, state=FSMAdmin.submit)

