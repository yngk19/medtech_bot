from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from utils import messages


def menu_kb(adjust: int):
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=messages.BTN_DIALOG, callback_data="btn_dialog"))
	builder.add(InlineKeyboardButton(text=messages.BTN_DIAGNOSTICS, callback_data="btn_diagnostics"))
	builder.add(InlineKeyboardButton(text=messages.BTN_ANALYSES, callback_data="btn_analyses"))
	builder.add(InlineKeyboardButton(text=messages.BTN_FAQ, callback_data="btn_faq"))
	builder.add(InlineKeyboardButton(text=messages.BTN_FIRST_HELP, callback_data="btn_first_help"))
	builder.add(InlineKeyboardButton(text=messages.BTN_AUTH, callback_data="btn_auth"))
	builder.adjust(adjust)
	return builder.as_markup()