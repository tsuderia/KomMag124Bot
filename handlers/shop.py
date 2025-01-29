from aiogram import Router, Dispatcher, F
from aiogram.types import CallbackQuery

from utils.texts import shop_command_text

shop_router = Router()

@shop_router.callback_query(F.data == 'shop')
async def shop_command(callback: CallbackQuery):
    await callback.message.answer(text=shop_command_text, reply_markup=None)

def register_shop_handler(dp: Dispatcher):
    dp.include_router(shop_router)