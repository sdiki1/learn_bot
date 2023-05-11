from aiogram.dispatcher.filters.state import StatesGroup, State


class Start(StatesGroup):
    Start_command = State()
    Profile = State()
    About_bot = State()
    Start_learning = State()




class Use_List(StatesGroup):
    ChooseList = State()



class Create_New_List(StatesGroup):
    Upload = State()
    Get_name = State()
    Download = State()

class Registration(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()

class EditProfile(StatesGroup):
    E1 = State()
    E2 = State()
    E3 = State()
