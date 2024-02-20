from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton



def test_start_kb(text: str, callback_data: str):
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
	return builder.as_markup()