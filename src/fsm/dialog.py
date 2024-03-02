from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State



class DialogFSM(StatesGroup):
    request = State()
    dialog = State()
    

class DoctorFSM(StatesGroup):
    inDialog = State()