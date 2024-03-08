from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
import asyncio
import aiogram
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from constants.unauthuser import constants
from keyboards.unauthuser import keyboards
from fsm.unauthuser import states
from utils.save_answers import SaveAnswers
from utils.load_questions import LoadQuestions


router = Router()  


@router.callback_query(F.data == constants.CALLBACK_BTN_CANCEL)
async def Cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(state=None)
    file_ids = []
    menuImage = FSInputFile("/home/yusuf/Desktop/medbot/media/menu.jpg")
    result = await callback.message.answer_photo(menuImage,
                                      caption=constants.MENU,
                                      reply_markup=keyboards.MenuKeyboard()
    )
    file_ids.append(result.photo[-1].file_id)
