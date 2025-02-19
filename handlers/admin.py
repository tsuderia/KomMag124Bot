from aiogram import Router, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboards import admin_keyboard

from config import ADMIN_ID

admin_router = Router()

@admin_router.message(Command('admin'))
async def check_if_admin(message: Message) -> bool:
    if (str(message.from_user.id) == str(ADMIN_ID)):
        await message.answer(f"Добро пожаловать, {message.from_user.full_name}", reply_markup=admin_keyboard)
        return True
    else:
        await message.delete()
        return False

async def notify_about_new_ticket():
    pass


@admin_router.message(Command('tickets'))
async def view_all_questions(message: Message):
    pass


def register_admin_handler(dp: Dispatcher):
    dp.include_router(admin_router)