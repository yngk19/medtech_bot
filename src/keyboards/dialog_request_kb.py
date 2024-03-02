from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton



def dialog_request_kb():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text="Да, принять", callback_data="btn_start_dialog"))
	builder.add(InlineKeyboardButton(text="Отклонить", callback_data="btn_reject_dialog"))
	builder.adjust(2)
	return builder.as_markup()