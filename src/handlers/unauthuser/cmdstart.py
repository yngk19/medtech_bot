from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
import asyncio
import aiogram
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from constants.unauthuser import constants
from keyboards.unauthuser import keyboards


router = Router()  

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
  userData = await state.get_data()
  try:
    agreement = userData['agreement']
    if not agreement:
      await Agreement(message, state)
      return
  except:
    await Agreement(message, state)
    return
  file_ids = []
  menuImage = FSInputFile("/home/yusuf/Desktop/medbot/media/menu.jpg")
  result = await message.answer_photo(
    menuImage,
    caption=constants.MENU,
    reply_markup=keyboards.MenuKeyboard()
  )
  file_ids.append(result.photo[-1].file_id)



async def Agreement(message: Message, state: FSMContext):
  await message.answer(
    text=constants.AGREEMENT,
    reply_markup=keyboards.AgreementKeyboard()
  )


@router.callback_query(F.data == constants.CALLBACK_BTN_AGREEMENT_YES)
async def StartDiagnostics(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  await state.update_data(agreement=True)
  await cmd_start(callback.message, state)

@router.callback_query(F.data == constants.CALLBACK_BTN_AGREEMENT_NO)
async def StartDiagnostics(callback: CallbackQuery, state: FSMContext):
  await state.update_data(agreement=False)
  await Disagreement(callback.message, state)


async def Disagreement(message: Message, state: FSMContext):
  await state.update_data(agreement=False)
  await message.answer(
    text=constants.DISAGREEMENT,
  )