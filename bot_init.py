from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from cfg import *

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
