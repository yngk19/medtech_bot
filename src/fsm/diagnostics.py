from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State



class DiagnosticsFSM(StatesGroup):
    question = State()