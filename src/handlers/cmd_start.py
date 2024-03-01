from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
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



@router.callback_query(F.data == "btn_start_diagnostics")
async def StartDiagnostics(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(DiagnosticsFSM.question)
    questions_list = await load_questions()
    question = questions_list[0]
    await state.update_data(question_id=0)
    await state.update_data(questions=questions_list)
    await state.update_data(answers=[])
    await state.update_data(user_id=callback.message.from_user.id)
    await callback.message.delete()
    await Diagnostics(callback, state)


async def Diagnostics(callback: CallbackQuery, state: FSMContext):
    file_ids = []
    menuImage = FSInputFile("/app/media/menu.jpg")
    user_data = await state.get_data()
    question_id = user_data['question_id']
    questions = user_data['questions']
    user_id = user_data['user_id']
    question = questions[question_id]
    text = f"Вопрос №{question_id + 1} {question['text']}"
    result = await callback.message.answer_photo(menuImage,
                                      caption=text,
                                      reply_markup=answers_kb(question, 2)
    )
    file_ids.append(result.photo[-1].file_id)
    
    
@router.callback_query(StateFilter(DiagnosticsFSM.question), lambda c: c.data.startswith("answer:"))
async def answer_callback(callback: CallbackQuery, state: FSMContext):
    answer_id = int(callback.data.split(":")[1])
    user_data = await state.get_data()
    user_id = user_data['user_id']
    answers = user_data['answers']
    question_id = user_data['question_id']
    questions_list = user_data['questions']
    question = questions_list[question_id]
    answers.append([question['text'], question['answers'][answer_id - 1]['text']])
    if question_id  < len(questions_list) - 1:
        await state.update_data(question_id=question_id + 1)
        await state.update_data(answers=answers)
        await callback.message.delete()
        await Diagnostics(callback, state)
    else:
        await SaveAnswers(answers, user_id)
        await state.clear()
        await callback.message.delete()
        await DiagnosticsResults(callback)


async def DiagnosticsResults(callback: CallbackQuery):
    file_ids = []
    image_from_pc = FSInputFile("/app/media/menu.jpg")
    result = await callback.message.answer_photo(image_from_pc,
                                      caption=DIAGNOSTICS_RESULTS
    )
    file_ids.append(result.photo[-1].file_id)




