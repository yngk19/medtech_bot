from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State



class DialogFSM(StatesGroup):
    request = State()
    conversation = State()
    