from aiogram import Bot
from aiogram.types import Message



async def on_start(bot: Bot, message: Message):
	await bot.send_message(6462294430, 'Bot started')