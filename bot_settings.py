import logging
import os

from dotenv import load_dotenv, find_dotenv

from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv(find_dotenv())


storage = MemoryStorage()

bot = Bot(token=os.getenv('6492617116:AAGrh1aCW14kEy2x-xN4hPvKFQQkk1i2YQ8'))

dp = Dispatcher(
    bot=bot,
    storage=storage
)


logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())
