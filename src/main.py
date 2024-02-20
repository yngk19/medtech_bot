import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile, CallbackQuery
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.methods.set_my_commands import SetMyCommands


from config.config import *
from handlers import cmd_start
from utils.setup_commands import setup_commands

async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(BOT_TOKEN)
    await bot.set_my_commands(commands=setup_commands())
    dp = Dispatcher(storage=MemoryStorage())
        
    dp.include_router(cmd_start.router)


    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())