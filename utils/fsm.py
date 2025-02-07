from aiogram.fsm.state import State, StatesGroup


class SupportStates(StatesGroup):
    stranger = State()
    asking_question = State()
