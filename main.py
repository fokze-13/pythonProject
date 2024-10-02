import asyncio

from aiogram import Bot, types, Dispatcher
from direc.config import load_config
import logging
from direc.handlers import router

config = load_config()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=config.basic_format)
handler = logging.FileHandler(config.log_file)
logger.addHandler(handler)


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher(config=config)

    dp.include_routers(router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

