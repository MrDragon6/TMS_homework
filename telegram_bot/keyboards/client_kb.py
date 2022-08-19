from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки клавиатуры клиента
b1 = KeyboardButton('/menu')
b2 = KeyboardButton('/location')
b3 = KeyboardButton('/schedule')
# b4 = KeyboardButton('/send phone number', request_contact=True)
# b5 = KeyboardButton('/send location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)  # .row(b4, b5)
