from aiogram import types, Dispatcher

from create_bot import dp, bot
from keyboards import kb_client
from database import sqlite_db


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hey, bro! Wanna have some pizza?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Communication only through private messages, text me first: '
                            '\nhttps://t.me/BestBroPizzaBot')


async def pizza_schedule_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'M-Th 9-21, F-S 9-23')


async def pizza_location_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Timiryazeva 67, Minsk')


@dp.message_handler(commands=['menu'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_schedule_command, commands=['schedule'])
    dp.register_message_handler(pizza_location_command, commands=['location'])
    dp.register_message_handler(pizza_menu_command, commands=['menu'])
