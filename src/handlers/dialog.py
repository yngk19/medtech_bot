from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
import asyncio
import aiogram
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from fsm.dialog import DialogFSM, DoctorFSM
from utils import messages
from keyboards.dialog_request_kb import dialog_request_kb
from utils.load_doctors import GetDoctor
from main import dp

router = Router()


@router.callback_query(F.data == "btn_dialog")
async def StartDialog(callback: CallbackQuery, state: FSMContext, bot: Bot):
	await state.set_state(DialogFSM.request)
	doctors = await GetDoctor()
	doctor_id = int(doctors[0])
	await HandleRequest(doctor_id, state, bot, callback.from_user.id, callback.message)

async def HandleRequest(doctor_id: int, state: FSMContext, bot: Bot, patient_id: int, message: Message):
	context = dp.fsm.get_context(bot=bot, chat_id=doctor_id, user_id=doctor_id)
	doctorState = await context.get_state()
	if doctorState == DoctorFSM.inDialog:
		await message.answer(text="Врач пока не может разговаривать.")
	else:
		await context.update_data(patient_id=patient_id)
		await message.answer(text="Запрос отправлен. Ожидайте.")
		await bot.send_message(
			doctor_id,
			text=messages.DIALOG_REQUEST,
			reply_markup=dialog_request_kb()
		)


@router.callback_query(F.data == 'btn_start_dialog')
async def RequestDialog(callback: CallbackQuery, state: FSMContext, bot: Bot):
	await callback.message.delete()
	state_data = await state.get_data()
	patient_id = state_data['patient_id']
	await state.set_state(DoctorFSM.inDialog)
	await state.update_data(patient_id=patient_id)
	context = dp.fsm.get_context(bot=bot, chat_id=patient_id, user_id=patient_id)
	await context.set_state(DialogFSM.dialog)
	await context.update_data(doctor_id=callback.from_user.id)
	await bot.send_message(patient_id, text="Врач подключен к диалогу. Можете начать разговор.")
	await state.set_state(DoctorFSM.inDialog)

@router.callback_query(F.data == 'btn_reject_dialog')
async def RequestDialog(callback: CallbackQuery, state: FSMContext, bot: Bot):
	await callback.message.delete()
	state_data = await state.get_data()
	patient_id = state_data['patient_id']
	context = dp.fsm.get_context(bot=bot, chat_id=patient_id, user_id=patient_id)
	await context.clear()
	await bot.send_message(patient_id, text="Врач не может сейчас говорить.")


@router.message(StateFilter(DialogFSM.dialog))
async def HandleResponse(message: Message, state: FSMContext, bot: Bot):
	state_data = await state.get_data()
	doctor_id = state_data['doctor_id']
	await bot.send_message(doctor_id, text=message.text)

@router.message(StateFilter(DoctorFSM.inDialog))
async def HandleResponse(message: Message, state: FSMContext, bot: Bot):
	state_data = await state.get_data()
	doctor_id = state_data['patient_id']
	await bot.send_message(doctor_id, text=message.text)
