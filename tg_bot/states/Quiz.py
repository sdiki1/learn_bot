from aiogram.dispatcher.filters.state import State, StatesGroup


class state_Quiz(StatesGroup):
    quiz = State()
    quiz_done = State()
