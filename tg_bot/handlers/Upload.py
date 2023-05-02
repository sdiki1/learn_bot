import io
import os
import pandas as pd
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, only_back, start_now, upload_table
from tg_bot.states import Start, Create_New_List



async def start_hand(message: types.Message):
    await Create_New_List.Upload.set()
    await message.answer('Отправь .xlsx файл с таблицей сюда)', reply_markup=upload_table)


async def download_file(message: types.Message):
    os.makedirs(f"files/{message.from_user.id}",exist_ok=True )
    await message.document.download(destination_file=f"files/{message.from_user.id}/tmp.xslx")

    #data = pd.read_excel(f"files/{message.from_user.id}/tmp.xslx", usecols="A,E:F", encoding='utf8')
    #data.to_json(path_or_buf= f"files/{message.from_user.id}/tmp"+ '.json', orient='records')

    await message.answer("Я попытался загрузить файл, и у меня получилось")

def register_uploading_file(dp:Dispatcher):
    dp.register_message_handler(start_hand, state=Start.Start_learning, text="Создать новый список слов")
    dp.register_message_handler(download_file, state=Create_New_List.Upload, content_types=types.ContentType.DOCUMENT)

