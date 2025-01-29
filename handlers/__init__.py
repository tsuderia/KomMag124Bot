from aiogram import Dispatcher

from handlers.about_us import register_about_us_handler
from handlers.shop import register_shop_handler
from handlers.start import register_start_handler
from handlers.support import register_support_handler


def register_all_handlers(dp: Dispatcher):
    register_start_handler(dp)
    register_about_us_handler(dp)
    register_shop_handler(dp)
    register_support_handler(dp)
