from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
import asyncio
import aiogram
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils import messages 
from keyboards import menu_kb


router = Router()  

@router.message(Command("lk"))
async def cmd_start(message: Message, state: FSMContext):
  file_ids = []
  image_from_pc = FSInputFile("/app/media/menu.jpg")
  result = await message.answer_photo(
    image_from_pc,
    caption=GREETING,
    reply_markup=menu_kb.menu_kb(3)
  )
  file_ids.append(result.photo[-1].file_id)