from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State




class TestFSM(StatesGroup):
    menu = State()
    current_question = State()