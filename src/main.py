import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile, CallbackQuery
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.methods.set_my_commands import SetMyCommands
import redis.asyncio as redis

from config.config import *
from handlers import cmd_start, cmd_lk, diagnostics, dialog
from utils.setup_commands import setup_commands


if USE_CACHE:
    storage = RedisStorage.from_url(url=f"redis://{REDIS_HOST}:{REDIS_PORT}/0")
    dp = Dispatcher(storage=storage)
else:
    dp = Dispatcher(storage=MemoryStorage())


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(BOT_TOKEN)

    await bot.set_my_commands(commands=setup_commands())
    dp.include_router(cmd_start.router)
    dp.include_router(cmd_lk.router)
    dp.include_router(diagnostics.router)
    dp.include_router(dialog.router)

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())