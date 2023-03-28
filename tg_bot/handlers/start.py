import datetime

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, only_back
from tg_bot.states import Start


async def start_hand(message: types.Message):
    await Start.Start_command.set()
    await message.reply('Привет! Этот бот может помочь тебе изучать слова на иностранном языке!', reply_markup=start)



def register_start(dp: Dispatcher):
    dp.register_message_handler(start_hand, commands='start')




async def profile(message: types.Message):
    await Start.Profile.set()
    await message.reply(f'ID юзера: {message.from_user.id},\nID чата: {message.chat.id},\nВремя сейчас: {datetime.datetime.now()}', reply_markup=only_back)

def register_profile(dp:Dispatcher):
    dp.register_message_handler(profile, state=Start.Start_command, text='профиль')

def register_profile_back(dp: Dispatcher):
    dp.register_message_handler(start_hand, state=Start.Profile, text='назад')





