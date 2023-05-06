from aiogram import types
from tg_bot.models import Users, List, session, male

def create_keyboard(id:int):
    buttons = [
        types.InlineKeyboardButton(text="list1", callback_data="use_list1"),
        types.InlineKeyboardButton(text="list2", callback_data="use_list2")
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
