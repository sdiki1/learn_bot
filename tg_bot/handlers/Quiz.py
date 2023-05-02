
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, only_back, start_now, new_or_old_list
from tg_bot.states import Start, Create_New_List



async def new_or_old(message: types.Message):
    await Start.Start_learning.set()
    get_my_lists = 4 #we need to count, how many lists with words you have saved


    await message.answer(f'в данный момент у вас имеется {get_my_lists} списков слов, что вы хотите, использовать существующий список или создать новый?', reply_markup=new_or_old_list)

def register_new_or_old(dp: Dispatcher):
    dp.register_message_handler(new_or_old, state=Create_New_List.Upload, text="назад")
    dp.register_message_handler(new_or_old, state=Start.Start_command, text='🔝начать🔝')
    dp.register_message_handler(new_or_old, state=Start.About_bot, text='🔝начать сейчас🔝')





