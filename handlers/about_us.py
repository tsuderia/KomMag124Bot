from aiogram import Router, Dispatcher, F
from aiogram.types import CallbackQuery

from utils.texts import about_us_command_text, start_command_text, interest_command_text
from keyboards.keyboards import about_us_keyboard, main_menu_keyboard, interest_keyboard

about_us_router = Router()

@about_us_router.callback_query(F.data == 'about')
async def _(callback: CallbackQuery):
    await callback.message.edit_text(about_us_command_text, reply_markup=about_us_keyboard)

@about_us_router.callback_query(F.data == 'back_to_about')
async def _(callback: CallbackQuery):
    await callback.message.edit_text(about_us_command_text, reply_markup=about_us_keyboard)

@about_us_router.callback_query(F.data == 'interest')
async def _(callback: CallbackQuery):
    await callback.message.edit_text(text=interest_command_text, reply_markup=interest_keyboard)

@about_us_router.callback_query(F.data == 'back_to_main_menu')
async def _(callback: CallbackQuery):
    await callback.message.edit_text(text=start_command_text, reply_markup=main_menu_keyboard)

def register_about_us_handler(dp: Dispatcher):
    dp.include_router(about_us_router)