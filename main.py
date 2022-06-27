from aiogram import types
from aiogram.utils import executor
from config import dp
import logging
from handlers import callback, client, fsmAdminMenu, echo

client.register_handlers_client(dp)
callback.register_handler_callback(dp)
fsmAdminMenu.register_fsmadmin_handler(dp)

echo.register_echo_message(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

