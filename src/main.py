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
from utils.setup_commands import setup_commands
from handlers.unauthuser import cmdstart, checkup, cancel


if USE_CACHE:
    storage = RedisStorage.from_url(url=f"redis://{REDIS_HOST}:{REDIS_PORT}/0")
    dp = Dispatcher(storage=storage)
else:
    dp = Dispatcher(storage=MemoryStorage())


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(BOT_TOKEN)

    await bot.set_my_commands(commands=setup_commands())
    dp.include_router(cmdstart.router)
    dp.include_router(checkup.router)
    dp.include_router(cancel.router)

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())