from aiogram.utils import executor
import logging
from config import dp
from handlers import client, callback, extra, fsm_admin_mentor, admin
from database.bot_db import sql_create

admin.register_handlers_admin(dp)
fsm_admin_mentor.register_handlers_fsm_admin_mentor(dp)
client.register_handlers_client(dp)
callback.register_handler_callback(dp)

extra.register_handlers_extra(dp)


async def on_startup(_):
    sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
