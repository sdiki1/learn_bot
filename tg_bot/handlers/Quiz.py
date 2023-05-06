
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, only_back, start_now, new_or_old_list, create_keyboard
from tg_bot.states import Start, Create_New_List, Use_List
from tg_bot.models import Users, List, session, male


async def new_or_old(message: types.Message):
    await Start.Start_learning.set()
    get_my_lists = 4 #we need to count, how many lists with words you have saved


    await message.answer(f'в данный момент у вас имеется {get_my_lists} списков слов, что вы хотите, использовать существующий список или создать новый?', reply_markup=new_or_old_list)

def register_new_or_old(dp: Dispatcher):
    dp.register_message_handler(new_or_old, state=Create_New_List.Upload, text="назад")
    dp.register_message_handler(new_or_old, state=Start.Start_command, text='🔝начать🔝')
    dp.register_message_handler(new_or_old, state=Start.About_bot, text='🔝начать сейчас🔝')



async def choose_list(message: types.Message):
    await Use_List.ChooseList.set()
    user = session.query(Users).filter(Users.tg_user_id == message.from_user.id).first()
    data = session.query(List).filter(List.id_user == user.id)
    name_shets = []
    for i in data:
        if i.name_sheet not in name_shets:
            name_shets.append(i.name_sheet)
    print(*name_shets)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i in name_shets:
        keyboard.add(types.InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))


    await message.answer('Выберите пожалуйста лист, который вы хотели бы начать изучать сейчас):', reply_markup=keyboard)

async def callback(call: types.CallbackQuery):
    print('lol')
    print(call.data)


def register_choose_list(dp: Dispatcher):
    dp.register_message_handler(choose_list, state=Start.Start_learning, text="Использовать старый список")

def register_callback_choose_list(dp: Dispatcher):
    dp.register_callback_query_handler(callback, state=Use_List.ChooseList)


