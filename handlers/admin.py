from aiogram import Router, Dispatcher, F, Bot
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboards import admin_keyboard
from database.requests import get_all_tickets, get_ticket_to_reply, find_user_by_ticket_id, update_ticket_status


from config import ADMIN_ID


admin_router = Router()

@admin_router.message(Command('admin'))
async def check_if_admin(message: Message) -> bool:
    if str(message.from_user.id) == str(ADMIN_ID):
        await message.answer(f"Добро пожаловать, {message.from_user.full_name}", reply_markup=admin_keyboard)
        return True
    else:
        await message.delete()
        return False

async def notify_about_new_ticket():
    pass


@admin_router.message(F.text == "‼️ Показать все обращения")
async def show_all_questions(message: Message):
    if check_if_admin:
        tickets = await get_all_tickets(status=False)
        if not tickets:
            await message.answer("Обращений в поддержку нет.")
            return
        for ticket in tickets:
            ticket_info = f"ID: {ticket.id}\nsender: {ticket.user_id}\nmessage: {ticket.message_text}"
            await message.answer(ticket_info)
    else:
        pass

@admin_router.message(F.text == "Показать все нерешенные обращения")
async def show_unsolved_questions(message: Message):
    if check_if_admin:
        tickets = await get_all_tickets(status=True)
    if not tickets:
        await message.answer("Нет решенных обращений.")
        return
    for ticket in tickets:
        ticket_info = f"ID: {ticket.id}\nsender: {ticket.user_id}\nmessage: {ticket.message_text}"
        await message.answer(ticket_info)
        
@admin_router.message(Command("reply"))
async def reply_to_user(message: Message, bot: Bot):
    command_parts = message.text.split(" " ,2)

    if len(command_parts) < 3:
        await message.answer("Для ответа используйте команду /reply <ticket_id> <ваш ответ>")
        return

    ticket_id = command_parts[1]
    reply_text = command_parts[2]

    ticket = await get_ticket_to_reply(ticket_id=ticket_id)
    user = await find_user_by_ticket_id(ticket=ticket)

    if not ticket:
        await message.reply("Обращение не найдено")
        return

    if not user:
        await message.reply("Пользователь не найден")
        return

    if not reply_text:
        await message.reply("Текст ответа не найден")

    await bot.send_message(chat_id=user.telegram_id, text=f"Администратор ответил на ваше сообщение:\n\n{reply_text}")

    await update_ticket_status(ticket=ticket, status=True)

    await message.reply("Ответ отправлен пользователю, обращение закрыто.")


        
def register_admin_handler(dp: Dispatcher):
    dp.include_router(admin_router)