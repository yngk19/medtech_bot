from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton



def answers_kb(question: list, adjust: int):
	builder = InlineKeyboardBuilder()
	for answer in question['answers']:
	    builder.add(InlineKeyboardButton(text=answer['text'], callback_data=f"answer:{answer['id']}"))
	builder.adjust(adjust)
	return builder.as_markup()