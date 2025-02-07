from aiogram import Dispatcher, F, Router
from aiogram.types import CallbackQuery, Message

from database.database import create_ticket
from utils.texts import support_command_text
from utils.fsm import SupportStates
from aiogram.fsm.context import FSMContext

support_router = Router()


@support_router.callback_query(F.data == 'support')
async def support_command(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=support_command_text)
    await state.set_state(SupportStates.asking_question)

@support_router.message(SupportStates.asking_question)
async def _(message: Message, state: FSMContext):
    await state.update_data(question=message.text, telegram_id=message.from_user.id)
    data = await state.get_data()

    await create_ticket(sender_telegram_id=data["telegram_id"], message_text=data["question"])
    await message.answer(f'Ваш вопрос {data["question"]} отправлен менеджеру')
    await state.clear()

def register_support_handler(dp: Dispatcher):
    dp.include_router(support_router)
