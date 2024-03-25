from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
import asyncio
import aiogram
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import requests


from constants.unauthuser import constants
from keyboards.unauthuser import keyboards
from fsm.unauthuser import states
from utils.save_answers import SaveAnswers
from utils.load_questions import LoadQuestions
from filters.unauthuser import filters

router = Router()  


@router.callback_query(F.data == constants.CALLBACK_BTN_DIAGNOSTICS)
async def StartDiagnostics(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.Diagnostics.question)
    questionsList = await LoadQuestions()
    question = questionsList[0]
    await state.update_data(question_id=0)
    await state.update_data(questions=questionsList)
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
                                      reply_markup=keyboards.AnswersKeyboard(question)
    )
    file_ids.append(result.photo[-1].file_id)
    
    
@router.callback_query(StateFilter(states.Diagnostics.question), lambda c: c.data.startswith("answer:"))
async def AnswerHandler(callback: CallbackQuery, state: FSMContext):
    answer_id = int(callback.data.split(":")[1])
    user_data = await state.get_data()
    agreement = user_data['agreement']
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
        await callback.message.delete()
        await SaveAnswers(answers, user_id)
        await Form(callback, state)



async def Form(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.Diagnostics.contact)
    file_ids = []
    menuImage = FSInputFile("/app/media/menu.jpg")
    result = await callback.message.answer_photo(menuImage,
        caption=constants.CONTACT,
        reply_markup=keyboards.ContactKeyboard()
    )
    file_ids.append(result.photo[-1].file_id)


@router.message(filters.IsTrueContact(), StateFilter(states.Diagnostics.contact))
async def GetContactTrue(message: Message, state: FSMContext, phone: str):
    await state.update_data(contact=phone)
    await message.answer(
        text=constants.MAIL,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(states.Diagnostics.mail)

@router.message(StateFilter(states.Diagnostics.contact))
async def GetContactFake(message: Message, state: FSMContext):
    await message.answer(text="Введенный номер телефона либо не ваш либо некорректный")


@router.message(StateFilter(states.Diagnostics.mail), filters.IsTrueMail())
async def GetMailTrue(message: Message, state: FSMContext, mail: str):
    await state.update_data(mail=mail)
    await state.set_state(state=None)
    await message.delete()
    await DiagnosticsResults(message)

@router.message(StateFilter(states.Diagnostics.mail))
async def GetMailFake(message: Message, state: FSMContext):
    await message.answer(text="Введенная почта некорректна")



async def DiagnosticsResults(message: Message):
    file_ids = []
    menuImage = FSInputFile("/app/media/menu.jpg")
    with open("/app/db/" + "user_" + str(message.from_user.id) + ".txt", "r") as fp:
        s = "".join(fp.readlines())
    resp = GetDiagnos(s)
    text = ''
    if resp.status_code == 400:
        text = '''
            Извините, произошла какая-то ошибка. Обратитесь к врачу.
        '''
    else:
        text = resp.text 
    result = await message.answer_photo(
        menuImage,
        caption=text,
        reply_markup=keyboards.ResultsKeyboard()
    )
    file_ids.append(result.photo[-1].file_id)



def GetDiagnos(checkupResult):
    API_KEY = "AIzaSyACDgDdRuyt9r6vSU_KxHeSzWuyUofVUZ0"

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

    headers = {
        "Content-Type": "application/json"
    }
    result = f''' 
    Ты помощник врача-диагноста, твоя задача, быть ему полезным и с точность до 90% при имеющемся анамнезе предсказывать наиближайший диагноз, 
    далее я буду давать тебе вводную информацию, по которой ты сделаешь определенные выводы, имеется Пациент, он прошел тест 
    и ты делаешь результаты на основании его ответов, помоги врачу и составь рекомендацию и диагноз в формате текста, чтобы это было максимально профессионально, и уложись в 100 слов,
    ниже информация предоставленная пациентом: 
    {checkupResult}
    '''

    data = {
        "contents": [{
            "parts":[{
                "text": result
            }]
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response
