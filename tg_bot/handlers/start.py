import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, state
from tg_bot.keyboards import start, only_back, start_now
from tg_bot.states import Start, Registration, state_Quiz
from tg_bot.models import Users, List, session
import logging

logger = logging.getLogger(__name__)
async def start_hand(message: types.Message):
    await Start.Start_command.set()
    if(session.query(Users).filter(Users.tg_user_id == message.from_user.id).count() == 0):
        await Registration.Q1.set()
        await message.answer('Привет! Ты Первый раз пользуешься нашим Ботом! Этот бот может помочь тебе изучать слова на иностранном языке! Давай пройдём Регистрацию)')
        await message.answer('Введите своё имя:')
        logger.info(f"user_id {session.query(Users).filter(Users.tg_user_id == message.from_user.id).first().id}, /start + start registration")
    else:
        await message.answer('Привет! Этот бот может помочь тебе изучать слова на иностранном языке!', reply_markup=start)
        logger.info(f"user_id {session.query(Users).filter(Users.tg_user_id == message.from_user.id).first().id} -/start")




def register_start(dp: Dispatcher):
    dp.register_message_handler(start_hand, commands='start', state="*")
    dp.register_message_handler(start_hand, state=Start.Start_learning, text='Назад')
    dp.register_message_handler(start_hand, state=Start.About_bot, text='Назад')
    dp.register_message_handler(start_hand, state=Start.Profile, text='Назад')
    dp.register_message_handler(start_hand, state=state_Quiz.quiz_done, text='Назад')
    dp.register_message_handler(start_hand, state=state_Quiz.quiz, text='Назад')


async def profile(message: types.Message):
    user = session.query(Users).filter(Users.tg_user_id == message.from_user.id).first()
    await Start.Profile.set()
    await message.answer(f'ID чата: {message.chat.id},\nВаше имя: {user.name}, \nВаш возраст: {user.age}, \nВремя сейчас: {datetime.datetime.now()}', reply_markup=only_back)
    logger.info(f"get info about user, user_id:{user.id}")


def register_profile_back(dp: Dispatcher):
    dp.register_message_handler(profile, state=Start.Start_command, text='Профиль')




async def about_bot(message: types.Message):
    await Start.About_bot.set()
    logger.info(f"get info about bot, user_id:{session.query(Users).filter(Users.tg_user_id == message.from_user.id).first().id}")
    await message.answer(f'Это бот в Telegram, который помогает в запоминании слов. Он позволяет создавать словарь и добавлять слова, которые нужно запомнить. Бот будет отправлять вам слова а вы ему их переводы для запоминания. Слова отправляются в таблице .xlsx, в одном столбике - слово на иностранном языке, во втором - его перевод.', reply_markup=start_now)

def register_about_bot(dp:Dispatcher):
    dp.register_message_handler(about_bot, state=Start.Start_command, text='О боте')


