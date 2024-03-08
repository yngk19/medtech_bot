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


router = Router()  

@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
  result = await message.answer_photo(
    menuImage,
    caption=constants.HELP,
    reply_markup=keyboards.HelpKeyboard()
  )
  file_ids.append(result.photo[-1].file_id)




