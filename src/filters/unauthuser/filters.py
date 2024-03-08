from aiogram.filters import Filter
from aiogram.types import Message
import re


class IsTrueMail(Filter):
	async def __call__(self, message: Message):
		pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
		isEmail = (re.match(pattern, message.text) is not None)
		if isEmail:
			return {'mail': message.text}
		else:
			return False


class IsTrueContact(Filter):
	async def __call__(self, message: Message):
		if message.contact is not None:
			if message.contact.user_id == message.from_user.id:
				return {'phone': message.contact.phone_number}
			else:
				return False
		else:
			contact = message.text
			if contact[:2] == '+7' and all([s.isdigit() for s in contact[2:]]):
				return {'phone': contact}
			else:
				return False