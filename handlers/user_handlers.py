from aiogram import types

from bot_init import dp
from keyboards.reply_markups import *

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Добро пожаловать в WaterMarker!', reply_markup=main_menu)
