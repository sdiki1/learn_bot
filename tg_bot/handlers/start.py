import datetime

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, only_back, start_now
from tg_bot.states import Start


async def start_hand(message: types.Message):
    await Start.Start_command.set()
    await message.answer('Привет! Этот бот может помочь тебе изучать слова на иностранном языке!', reply_markup=start)



def register_start(dp: Dispatcher):
    dp.register_message_handler(start_hand, commands='start')




async def profile(message: types.Message):
    await Start.Profile.set()
    await message.answer(f'ID юзера: {message.from_user.id},\nID чата: {message.chat.id},\nВремя сейчас: {datetime.datetime.now()}', reply_markup=only_back)

def register_profile(dp:Dispatcher):
    dp.register_message_handler(profile, state=Start.Start_command, text='профиль')

def register_profile_back(dp: Dispatcher):
    dp.register_message_handler(start_hand, state=Start.Profile, text='назад')


async def about_bot(message: types.Message):
    await Start.About_bot.set()
    await message.answer(f'Это бот в Telegram, который помогает в запоминании слов. Он позволяет создавать словарь и добавлять слова, которые нужно запомнить. Бот будет отправлять вам слова а вы ему их переводы для запоминания. Слова отправляются в таблице .xlsx, в одном столбике - слово на иностранном языке, во втором - его перевод.', reply_markup=start_now)

def register_about_bot(dp:Dispatcher):
    dp.register_message_handler(about_bot, state=Start.Start_command, text='О боте')

def register_about_bot_back(dp: Dispatcher):
    dp.register_message_handler(start_hand, state=Start.About_bot, text='назад')





