import asyncio
import logging
from aiogram import Bot, Dispatcher

from settings import setting
from utils.handlers import handlers


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=setting.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
