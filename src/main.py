import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
#from aiogram.fsm.storage.redis import RedisStorage


from config import config
from handlers import on_start

async def main() -> None:
    logging.basicConfig(level=logging.DEBUG, 
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(config.BOT_TOKEN, parse_mode="HTML")

    '''
    if config.fsm_mode == "redis":
        storage = RedisStorage.from_url(
            url=,
            connection_kwargs={"decode_responses": True}
        )
    else:
        storage = MemoryStorage()
    '''
    storage = MemoryStorage()

    dp = Dispatcher(storage=storage, config=config)

    dp.startup.register(on_start)
    #dp.include_router(default_commands.router)
    #dp.include_router(spin.router)
    
    #await set_bot_commands(bot, l10n)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())