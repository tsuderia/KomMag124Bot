from sqlalchemy import select, update
from database.models import async_session
from database.models import Ticket, User

def connection(func):
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper


@connection
async def get_current_user(session, sender_telegram_id: int):
    result = await session.execute(select(User).where(User.telegram_id==sender_telegram_id))
    current_user = result.scalars().first()
    
    if current_user is not None:
        return current_user
    else:
        print("user doesnt exist")
        return None

@connection
async def check_user_exist(session, sender_telegram_id: int) -> bool:
    result = await session.exxcute(select(User).where(User.telegram_id==sender_telegram_id))
    user = result.scalars().first()

    if user is not None:
        return True
    else:
        return False
        
@connection
async def create_ticket(session, sender_telegram_id: int, message_text: str):
    user = await get_current_user(sender_telegram_id=sender_telegram_id)
    ticket = Ticket(user=user, message_text=message_text, status=False)
    try:
        session.add(ticket)
        await session.commit()
    except Exception:
        print("could not add create a ticket")
        
        
@connection
async def add_user(session, telegram_id: int, username: str):

    user: User = await get_current_user(telegram_id)
    
    if user is not None:
        print("User already exists")
        return

    user = User(telegram_id=telegram_id, username=username)
    session.add(user)
    await session.commit()

    print("User successfully added!!")


@connection
async def get_all_tickets(session, status: bool = False):
    result = await session.execute(select(Ticket).where(Ticket.status == status))
    tickets = result.scalars().all()
    return tickets


@connection
async def get_ticket_to_reply(session, ticket_id: int):
    result = await session.execute(select(Ticket).where(Ticket.id == ticket_id))
    ticket = result.scalars().first()
    return ticket


@connection
async def find_user_by_ticket_id(session, ticket: Ticket):
    result = await session.execute(select(User).where(User.id == ticket.user_id))
    user = result.scalars().first()
    return user

@connection
async def update_ticket_status(session, ticket: Ticket, status: bool):

    await session.execute(update(Ticket).where(Ticket.id == ticket.id).values(status=status))
    await session.commit()