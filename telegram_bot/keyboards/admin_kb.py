from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки клавиатуры админа
button_load = KeyboardButton('/add_pizza')
button_delete = KeyboardButton('/delete_pizza')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(button_load).add(button_delete)
