from aiogram import Router, Dispatcher, F
from aiogram.types import CallbackQuery

from utils.texts import shop_command_text
from keyboards.keyboards import shop_keyboard

shop_router = Router()

@shop_router.callback_query(F.data == 'shop')
async def shop_command(callback: CallbackQuery):
    await callback.message.answer(text=shop_command_text, reply_markup=shop_keyboard)

@shop_router.callback_query(F.data == 'show_items')
async def _(callback: CallbackQuery):
    await callback.message.answer(text='Здесь будет список товаров (наверное, что-то я не придумал как он должен выглядеть)')

def register_shop_handler(dp: Dispatcher):
    dp.include_router(shop_router)