from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State



class Diagnostics(StatesGroup):
    question = State()
    contact = State()
    mail = State()


class Help(StatesGroup):
    inDialog = State()
    

