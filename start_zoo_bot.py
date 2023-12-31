import logging

from datetime import datetime
from aiogram import executor

from bot_settings import dp

from handlers import (
    quiz_handlers,
    static_commands_handlers,
)


# --------

async def on_startup(dp):
    logging.info(f' {datetime.now()} : Bot is active.')


# --------

quiz_handlers.register_quiz_handlers(disp=dp)
static_commands_handlers.register_static_command_handlers(disp=dp)


# ---------

async def on_shutdown(dp):
    logging.warning(f' {datetime.now()} : Shutting down...')


# -------

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
