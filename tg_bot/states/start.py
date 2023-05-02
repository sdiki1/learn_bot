from aiogram.dispatcher.filters.state import StatesGroup, State


class Start(StatesGroup):
    Start_command = State()
    Profile = State()
    About_bot = State()
    Start_learning = State()


class Use_Old_List(StatesGroup):
    ChooseList = State()


class Create_New_List(StatesGroup):
    Upload = State()
