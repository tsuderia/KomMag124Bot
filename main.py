import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from handlers import register_all_handlers
import logging

async def main():

    # registering bot
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # registering dispatcher
    dp = Dispatcher()

    # registering all routers & handlers
    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await bot.session.close()
        print("Бот отключен")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

