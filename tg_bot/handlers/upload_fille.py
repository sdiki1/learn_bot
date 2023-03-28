from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


async def upload_file(message:types.Message):

    if message.text == 'file':
        message.reply('you uploaded file')



def register_uploading(dp: Dispatcher):
    dp.register_message_handler(upload_file, text='file')

