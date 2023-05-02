

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, only_back, start_now, upload_table
from tg_bot.states import Start, Create_New_List

async def start_hand(message: types.Message):
    await Create_New_List.Upload.set()
    await message.answer('Отправь .xlsx файл с таблицей сюда)', reply_markup=upload_table)




