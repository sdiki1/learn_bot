from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, state
from aiogram.types import ReplyKeyboardRemove

from tg_bot.keyboards import start, choose_male
from tg_bot.states import EditProfile
from tg_bot.models import Users, List, session, male
import logging



