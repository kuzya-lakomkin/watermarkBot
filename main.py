from bot_init import *
from handlers import *

from aiogram.utils import executor


if __name__ == '__main__':
    executor.start_polling(dp)
