from aiogram.utils import executor
import logging
from config import dp
from handlers import client, callback, extra, fsm_admin_mentor

fsm_admin_mentor.register_handlers_fsm_admin_mentor(dp)
client.register_handlers_client(dp)
callback.register_handler_callback(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
