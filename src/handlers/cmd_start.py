from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
import asyncio
import aiogram
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.messages import GREETING, BTN_START_TEST
from utils.load_questions import load_questions
from utils.save_answers import save_answers
from fsm.test import TestFSM
from keyboards.test_kb import test_start_kb
from keyboards.answers_kb import answers_kb


router = Router()  

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
  await state.clear()
  await state.set_state(TestFSM.menu)
  await state.update_data(question_id=0)
  await state.update_data(answers=[])
  await state.update_data(user_id=message.from_user.id)
  file_ids = []
  image_from_pc = FSInputFile("/app/media/menu.jpg")
  result = await message.answer_photo(
    image_from_pc,
    caption=GREETING,
    reply_markup=test_start_kb(BTN_START_TEST, "btn_test")
  )
  file_ids.append(result.photo[-1].file_id)



@router.callback_query(TestFSM.menu, F.data == "btn_test")
async def send_question(callback: CallbackQuery, state: FSMContext):
    file_ids = []
    image_from_pc = FSInputFile("/app/media/menu.jpg")
    user_data = await state.get_data()
    question_id = user_data['question_id']
    answers = user_data['answers']
    user_id = user_data['user_id']
    questions_list = await load_questions()
    question = questions_list[question_id]
    text = f"Вопрос №{question_id + 1} {question['text']}"
    await state.set_state(TestFSM.current_question)
    await state.update_data(question_id=question_id)
    await state.update_data(answers=answers)
    await state.update_data(user_id=user_id)
    await callback.message.delete()
    result = await callback.message.answer_photo(image_from_pc,
                                      caption=text,
                                      reply_markup=answers_kb(question, 2)
    )
    file_ids.append(result.photo[-1].file_id)

    
    
@router.callback_query(StateFilter(TestFSM.current_question), lambda c: c.data.startswith("answer:"))
async def answer_callback(callback: CallbackQuery, state: FSMContext):
    answer_id = int(callback.data.split(":")[1])
    questions_list = await load_questions()
    user_data = await state.get_data()
    user_id = user_data['user_id']
    question_id = user_data['question_id']
    answers = user_data['answers']
    question = questions_list[question_id]
    answers.append([question['text'], question['answers'][answer_id - 1]['text']])
    if question_id  < len(questions_list) - 1:
        await state.update_data(question_id=question_id + 1)
        await state.update_data(answers=answers)
        await send_question(callback, state)
    else:
        await save_answers(answers, user_id)
        await state.clear()
        await callback.message.delete()
        await cmd_start(callback.message, state)



























"""
@router.message_handler(Command("start"))
async def start_command(message: Message):
    # Сброс состояния пользователя
    await TestFSM.reset_state(chat=message.chat.id)
    
    # Загрузка вопросов
    questions = await load_questions()
    
    # Начало теста
    await TestFSM.current_question.set()
    await send_question(message, questions[0])

async def send_question(message: Message, question):
    text = f"**Вопрос:** {question['text']}"
    
    buttons = []
    for answer in question['answers']:
        buttons.append(
            aiogram.types.InlineKeyboardButton(
                text=answer['text'],
                callback_data=f"answer:{answer['id']}"
            )
        )
    await message.answer(text, reply_markup=aiogram.types.InlineKeyboardMarkup(inline_keyboard=buttons))

@router.callback_query(lambda c: c.data.startswith("answer:"))
async def answer_callback(callback_query: CallbackQuery, state: FSMContext):
    answer_id = int(callback_query.data.split(":")[1])
    
    user_answers[callback_query.message.message_id] = answer_id
    
    questions = await load_questions()
    current_question_index = user_answers.get(callback_query.message.message_id)
    
    if current_question_index < len(questions) - 1:
        await TestFSM.current_question.set()
        await send_question(callback_query.message, questions[current_question_index + 1])
    else:
        await TestFSM.answer.set()
        await callback_query.message.answer("Тест завершен!")
"""