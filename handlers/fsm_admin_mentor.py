from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from keyboards import client_kb
from database.bot_db import sql_command_insert



class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    age = State()
    course = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.id.set()
        await message.answer('HI 👋\n'
                             'Please write the ID of mentor.', reply_markup=client_kb.cancel_marcup)
    elif message.from_user.id not in ADMINS:
        await message.answer('You are not a curator!')
    else:
        await message.answer('Write to private!')


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = int(message.text)
    await FSMAdmin.next()
    await message.answer('What is the name of mentor?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('How old is the mentor?')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMAdmin.next()
    await message.answer("What is the mentor's course?")


async def load_course(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['course'] = message.text
    await FSMAdmin.next()
    await message.answer("What is the mentor's group?")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"ID: {data['id']} \n"
                             f"Name: {data['name']}\n"
                             f"Age: {data['age']}\n"
                             f"Course: {data['course']}\n"
                             f"Group: {data['group']}")
    await FSMAdmin.next()
    await message.answer('Please check your answers,are they correct?', reply_markup=client_kb.submit_markup)


async def submit_fsm(message: types.Message, state: FSMContext):
    if message.text.lower() == 'yes':
        await sql_command_insert(state)
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
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_course, state=FSMAdmin.course)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit_fsm, state=FSMAdmin.submit)
