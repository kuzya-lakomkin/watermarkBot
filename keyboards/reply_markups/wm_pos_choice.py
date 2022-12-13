from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# выбор расположения водного знака
rigth_top = KeyboardButton('Правый верхний угол')
left_top = KeyboardButton('Левый верхний угол')
right_bottom = KeyboardButton('Правый нижний угол')
left_bottom = KeyboardButton('Левый нижний угол')
center = KeyboardButton('По центру')

pos_choice = ReplyKeyboardMarkup(resize_keyboard=True)
pos_choice.row([rigth_top, left_top])
pos_choice.row([right_bottom, left_bottom])
pos_choice.add(center)
