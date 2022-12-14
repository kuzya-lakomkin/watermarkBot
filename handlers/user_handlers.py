from aiogram import types

from bot_init import dp
from keyboards.reply_markups import *
from states import *


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await message.reply('Добро пожаловать в WaterMarker!', reply_markup=main_menu)
    await state.set_state(PreprocessingStates.START)


@dp.message_handler(state=PreprocessingStates.START)
async def links_input(message: types.Message):
    if message.text not in [button.text for button in buttons]:
        await message.reply('Ошибка! Неизвестная команда.')
    else:
        await message.reply('Отлично! Теперь введите ссылки на интересующие Вас Telegram-каналы.',
                            reply_markup=types.ReplyKeyboardRemove())
        await PreprocessingStates.LINKS_INPUT.set()
