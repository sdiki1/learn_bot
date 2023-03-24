from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


async def start(message: types.Message):
    await message.reply('Hello, this bot will help you to learn some English words!')

def register_start(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart(deep_link="123"))


