from aiogram import Router, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.texts import start_command_text
from keyboards.keyboards import main_menu_keyboard

start_router = Router()

@start_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(start_command_text, reply_markup=main_menu_keyboard)

def register_start_handler(dp: Dispatcher):
    dp.include_router(start_router)