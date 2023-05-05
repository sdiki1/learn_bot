import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, choose_male
from tg_bot.states import Start, Registration
from tg_bot.models import Users, List, session, male



async def enter_age(message:types.message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data["name"] = answer
    await message.answer(f"Хорошо, {answer},\nТеперь введите свой возраст:", reply_markup=None)

    await Registration.Q2.set()


async def enter_male(message: types.message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["age"] = answer
    await message.answer(f"Введите свой пол:", reply_markup=choose_male)
    await Registration.Q3.set()

async def start_hand(message: types.Message, state: FSMContext):
    if message.text not in ["Мужчина", "Женщина", "Не указывать"]:
        await Registration.Q2.set()
        return

    async with state.proxy() as data:
        if message.text == "Мужчина":
            data["male"] = male.male
        elif message.text == "Женщина":
            data["male"] = male.female
        else:
            data["male"] = male.dont_know
    data=await state.get_data()
    new_user = Users(name=f'{data["name"]}', tg_user_id=message.from_user.id, tg_user_chat_id=message.chat.id, age=data["age"], male=data["male"])
    session.add(new_user)
    session.commit()
    await Start.Start_command.set()
    await message.answer('Привет! Этот бот может помочь тебе изучать слова на иностранном языке!', reply_markup=start)




def register_registration(dp: Dispatcher):
    dp.register_message_handler(enter_age, state=Registration.Q1)
    dp.register_message_handler(enter_male, state=Registration.Q2)
    dp.register_message_handler(start_hand, state=Registration.Q3)


