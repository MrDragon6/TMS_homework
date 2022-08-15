from aiogram import types, Dispatcher
from create_bot import dp


async def echo_send(message: types.Message):
    if message.text == 'Что ты умеешь?':
        await message.reply('I can sell you pizza')
    else:
        await message.reply('Enough talking, order some pizza! Type "I want pizza"')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
