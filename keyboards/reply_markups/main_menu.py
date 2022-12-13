from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# меню при входе
buttons = [KeyboardButton('Начать')]
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(buttons)
