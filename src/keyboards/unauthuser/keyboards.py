from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardBuilder
from constants.unauthuser import constants


def MenuKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_DIAGNOSTICS, callback_data=constants.CALLBACK_BTN_DIAGNOSTICS))
	builder.add(InlineKeyboardButton(text=constants.BTN_APPOINTMENTS, callback_data=constants.CALLBACK_BTN_APPOINTMENTS))
	builder.add(InlineKeyboardButton(text=constants.BTN_HELP, callback_data=constants.CALLBACK_BTN_HELP))
	builder.add(InlineKeyboardButton(text=constants.BTN_OTHER, callback_data=constants.CALLBACK_BTN_OTHER))
	builder.adjust(1)
	return builder.as_markup()

def AuthKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_AUTH_PATIENT, callback_data=constants.CALLBACK_BTN_AUTH_PATIENT))
	builder.add(InlineKeyboardButton(text=constants.BTN_AUTH_ADMIN, callback_data=constants.CALLBACK_BTN_AUTH_ADMIN))
	builder.adjust(1)
	return builder.as_markup()


def HelpKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_CANCEL, callback_data=constants.CALLBACK_BTN_CANCEL))
	builder.adjust(1)
	return builder.as_markup()


def AnswersKeyboard(question: list):
	builder = InlineKeyboardBuilder()
	for answer in question['answers']:
	    builder.add(InlineKeyboardButton(text=answer['text'], callback_data=f"answer:{answer['id']}"))
	builder.adjust(2)
	return builder.as_markup()

def ResultsKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_APPOINTMENT, callback_data=constants.CALLBACK_BTN_APPOINTMENT))
	builder.add(InlineKeyboardButton(text=constants.BTN_USEFUL_RESOURCES, callback_data=constants.CALLBACK_BTN_USEFUL_RESOURCES))
	builder.add(InlineKeyboardButton(text=constants.BTN_INFO, callback_data=constants.CALLBACK_BTN_INFO))
	builder.add(InlineKeyboardButton(text=constants.BTN_CANCEL, callback_data=constants.CALLBACK_BTN_CANCEL))
	builder.adjust(1)
	return builder.as_markup()


def AgreementKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_AGREEMENT_YES, callback_data=constants.CALLBACK_BTN_AGREEMENT_YES))
	builder.add(InlineKeyboardButton(text=constants.BTN_AGREEMENT_NO, callback_data=constants.CALLBACK_BTN_AGREEMENT_NO))
	builder.adjust(2)
	return builder.as_markup()


def ContactKeyboard():
	builder = ReplyKeyboardBuilder()
	builder.row(KeyboardButton(text="Отправить контакт", request_contact=True))
	return builder.as_markup()
