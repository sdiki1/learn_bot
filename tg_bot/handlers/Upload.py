
import os, xlrd
from aiogram import types, Dispatcher
from tg_bot.keyboards import upload_table
from tg_bot.states import Start, Create_New_List
from tg_bot.models import Users, List, session





async def upload_to_base(path: str, id_user: int, name_table: str):

    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_index(0)

    print(worksheet.cell(1, 1).value)    # cell(y, x).value

    user = session.query(Users).filter(Users.tg_user_id == id_user).first()
    for i in range(worksheet.nrows):

        new_list = List(id_user=user.id, word=worksheet.cell(i, 0).value, translate=worksheet.cell(i, 1).value, name_sheet=name_table)
        session.add(new_list)
        session.commit()






async def start_hand(message: types.Message):
    await Create_New_List.Upload.set()
    await message.answer('Отправь .xlsx файл с таблицей сюда)', reply_markup=upload_table)


async def save_file_getname(message: types.Message):
    await Create_New_List.Get_name.set()
    os.makedirs(f"files/{message.from_user.id}",exist_ok=True )
    await message.document.download(destination_file=f"files/{message.from_user.id}/tmp.xsl")

    await message.answer("Введите название таблицы:")






async def install_data(message: types.Message):
    await Create_New_List.Download.set()

    await upload_to_base(f"files/{message.from_user.id}/tmp.xsl", message.from_user.id, message.text)
    await message.answer("Я попытался загрузить файл, и у меня получилось")



def register_uploading_file(dp:Dispatcher):
    dp.register_message_handler(start_hand, state=Start.Start_learning, text="Создать новый список слов")
    dp.register_message_handler(save_file_getname, state=Create_New_List.Upload, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(install_data, state=Create_New_List.Get_name)

