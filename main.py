import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from database.models import init_db

from config import BOT_TOKEN
import handlers
import logging

# registering bot

async def main():

    # init db
    await init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # registering dispatcher
    dp = Dispatcher()

    # registering all routers & handlers
    handlers.register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await bot.session.close()
        print("Бот отключен")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

