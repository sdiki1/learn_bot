from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode



async def bot_echo(message: types.Message):
    text = [
        "Эхо сообщение без состояния",
        "Сообщение:",
        message.text,
        f"Id_user: {message.from_user.id}",]

    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
