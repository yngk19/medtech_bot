from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
import asyncio
import aiogram
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.messages import GREETING, BTN_START_DIAGNOSTICS, DIAGNOSTICS_RESULTS
from utils.load_questions import load_questions
from utils.save_answers import SaveAnswers
from fsm.diagnostics import DiagnosticsFSM
from keyboards.diagnostics_kb import diagnostics_kb
from keyboards.answers_kb import answers_kb


router = Router()  


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
  file_ids = []
  image_from_pc = FSInputFile("/app/media/menu.jpg")
  result = await message.answer_photo(
    image_from_pc,
    caption=GREETING,
    reply_markup=diagnostics_kb(BTN_START_DIAGNOSTICS, "btn_start_diagnostics")
  )
  file_ids.append(result.photo[-1].file_id)




