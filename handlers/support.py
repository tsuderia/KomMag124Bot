from aiogram import Dispatcher, F, Router
from aiogram.types import CallbackQuery

from utils.texts import support_command_text

support_router = Router()

@support_router.callback_query(F.data == 'support')
async def support_command(callback: CallbackQuery):
    await callback.message.answer(text=support_command_text)

def register_support_handler(dp: Dispatcher):
    dp.include_router(support_router)
