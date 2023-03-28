from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from tg_bot.keyboards import start



async def start_hand(message: types.Message):
    await message.answer('Привет! Этот бот может помочь тебе изучать слова на иностранном языке!', reply_markup=start)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start_hand, commands='start')




