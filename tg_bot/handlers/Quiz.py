
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, state
from aiogram.types import KeyboardButton

from tg_bot.keyboards import start, only_back, start_now, new_or_old_list,  back_new_or_old
from tg_bot.states import Start, Create_New_List, Use_List, state_Quiz
from tg_bot.models import Users, List, session, male


async def new_or_old(message: types.Message):
    await Start.Start_learning.set()

    user = session.query(Users).filter(Users.tg_user_id == message.from_user.id).first()
    data = session.query(List).filter(List.id_user == user.id)
    name_shets = []
    for i in data:
        if i.name_sheet not in name_shets:
            name_shets.append(i.name_sheet)
    get_my_lists = len(name_shets)
    await message.answer(f'В данный момент у вас имеется {get_my_lists} списков слов, что вы хотите, использовать существующий список или создать новый?', reply_markup=new_or_old_list)

def register_new_or_old(dp: Dispatcher):
    dp.register_message_handler(new_or_old, state=Create_New_List.Download, text="Назад")
    dp.register_message_handler(new_or_old, state=Use_List.ChooseList, text="Назад")
    dp.register_message_handler(new_or_old, state=Create_New_List.Upload, text="Назад")
    dp.register_message_handler(new_or_old, state=Start.Start_command, text='🔝Начать🔝')
    dp.register_message_handler(new_or_old, state=Start.About_bot, text='🔝Начать сейчас🔝')



async def choose_list(message: types.Message):
    await Use_List.ChooseList.set()
    user = session.query(Users).filter(Users.tg_user_id == message.from_user.id).first()
    data = session.query(List).filter(List.id_user == user.id)
    name_shets = []
    for i in data:
        if i.name_sheet not in name_shets:
            name_shets.append(i.name_sheet)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i in name_shets:
        keyboard.add(types.InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))

    await message.answer(f"У вас имеется {len(name_shets)} списков слов!", reply_markup=only_back)
    await message.answer('Выберите пожалуйста лист, который вы хотели бы начать изучать сейчас):', reply_markup=keyboard)



async def callback(call: types.CallbackQuery, state = FSMContext):
    await state_Quiz.quiz.set()
    await call.message.answer(f'Вы решили изучать список под названием: {call.data}', reply_markup=only_back)
    await call.message.answer(f'Суть нашего изучения: мы вам даем слово на русском языке, вы вводите его перевод)', reply_markup=only_back)
    user = session.query(Users).filter(Users.tg_user_id == call.message.from_user.id).first()
    data1 = session.query(List).filter(List.id_user == 1)
    datal = data1.filter(List.name_sheet == call.data).all()

    async with state.proxy() as data:
        data["current"] = 0
        data["words_all"] = datal
        data["words_grade1"] = []
        data["words_grade2"] = []
        data["incorrect"] = 0
        await call.message.answer(f'Первое слово: \n{data["words_all"][data["current"]].word}', reply_markup=only_back)


async def qquiz(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if(data["words_all"] is not None and data["current"] < (len(data["words_all"]))):
            if (message.text == data["words_all"][data["current"]].translate and data["current"] < (len(data["words_all"]) -1)):
                data["current"] += 1
                if(data["incorrect"] > 0):
                    data["words_grade1"].append(data["current"] - 1)
                    data["incorrect"] = 0
                await message.answer(f'Ещё одно слово: \n{data["words_all"][data["current"]].word}', reply_markup=only_back)
            elif(data["incorrect"] < 3 and data["current"] < (len(data["words_all"]) -1)):
                data["incorrect"] += 1
                await message.answer(f'Неверно, попробуйте ещё раз', reply_markup=only_back)
            elif(data["current"] < (len(data["words_all"]) -1)):
                data["words_grade2"].append(data["current"])
                await message.answer(f'Верный ответ:{data["words_all"][data["current"]].translate}', reply_markup=only_back)
                data["current"] += 1
                data["incorrect"] = 0
                await message.answer(f'Ещё одно слово: \n{data["words_all"][data["current"]].word}',
                                     reply_markup=only_back)
            elif(message.text == data["words_all"][data["current"]].translate):
                data["current"] += 1
                if (data["words_grade2"] is not None and data["words_grade1"] is not None):
                    dataa = []
                    for i in data["words_grade2"]:
                        dataa.append(data["words_all"][i])
                    for i in data["words_grade1"]:
                        dataa.append(data["words_all"][i])
                    for i in data["words_grade2"]:
                        dataa.append(data["words_all"][i])
                    data["words_all"] = dataa
                    data["words_grade1"].clear()
                    data["words_grade2"].clear()
                    data["current"] = 0
                    data["incorrect"] = 0
                    try:
                        print(f"LOL       {data['current']}           {data['words_all']}")
                        await message.answer(f'Ещё слово:\n{data["words_all"][data["current"]].word}',
                                             reply_markup=only_back)
                    except:
                        await state_Quiz.quiz_done.set()
                        await message.answer(f'УРА, вы почти выучили все слова)', reply_markup=only_back)
                else:
                    await state_Quiz.quiz_done.set()
                    await message.answer(f'УРА, вы почти выучили все слова)', reply_markup=only_back)

            else:
                await message.answer(f'Неверно, попробуйте ещё раз', reply_markup=only_back)

        elif( data["words_grade2"] is not None and data["words_grade1"] is not None ):
            dataa = []
            for i in data["words_grade2"]:
                dataa.append(data["words_all"][i])
            for i in data["words_grade1"]:
                dataa.append(data["words_all"][i])
            for i in data["words_grade2"]:
                dataa.append(data["words_all"][i])
            data["words_all"] = dataa
            data["words_grade1"].clear()
            data["words_grade2"].clear()
            data["current"] = 0
            data["incorrect"] = 0
            try:
                print(f"LOL       {data['current']}           {            data['words_all']        }")
                await message.answer(f'Ещё слово:\n{data["words_all"][data["current"]].word}',
                                          reply_markup=only_back)
            except:
                await state_Quiz.quiz_done.set()
                await message.answer(f'УРА, вы почти выучили все слова)', reply_markup=only_back)
        else:
            await state_Quiz.quiz_done.set()
            await message.answer(f'УРА, вы почти выучили все слова)', reply_markup=only_back)











def register_choose_list(dp: Dispatcher):
    dp.register_message_handler(choose_list, state=Start.Start_learning, text="Использовать старый список")


def register_callback_choose_list(dp: Dispatcher):
    dp.register_callback_query_handler(callback, state=Use_List.ChooseList)
    dp.register_message_handler(qquiz, state=state_Quiz.quiz)


