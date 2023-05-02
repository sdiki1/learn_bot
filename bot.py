import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tg_bot.handlers import register_start, register_profile_back, \
    register_about_bot, register_new_or_old
from tg_bot.config import load_config
from tg_bot.filters.admin import AdminFilter
from tg_bot.handlers.echo import register_echo
from tg_bot.middlewares.db import DbMiddleware

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Untitled.db")
Session = sessionmaker()
session = Session(bind=engine)



logger = logging.getLogger(__name__)

def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware)

def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)

def register_all_handlers(dp):
    register_start(dp)
    register_echo(dp)

    register_profile_back(dp)
    register_about_bot(dp)
    register_new_or_old(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=MemoryStorage())
    bot['config'] = config

    #register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storager.close()
        await dp.storage.wait_closed()
        await bot.session.close()



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

