from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="6026709005:AAHwgB0cfI8A5C8_x2GKOuubCyXg54C43XI")
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Привет, это БОТ для изучения слов на английском языке! "
    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())

executor.start_polling(dp)

