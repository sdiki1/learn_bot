from aiogram.dispatcher.filters.state import StatesGroup, State


class Start(StatesGroup):
    Start_command = State()
    Profile = State()
    About_bot = State()
    Start_learning = State()
