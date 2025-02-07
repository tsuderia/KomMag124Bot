from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, BigInteger
from sqlalchemy import select
from config import DB_URL

engine = create_async_engine(DB_URL, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=True)
    
class Ticket(Base):
    __tablename__ = 'tickets'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sender_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    message_text: Mapped[str] = mapped_column(String(256))
    
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def create_ticket(sender_telegram_id: int, message_text: str):
    async with async_session() as session:
        async with session.begin():
            ticket = Ticket(sender_telegram_id=sender_telegram_id, message_text=message_text)
            try:
                session.add(ticket)
                await session.commit()
            except Exception:
                print("WATAFAK MATAFAK WE CRASH")

async def get_all_tickets() -> list[Ticket]:
    async with async_session() as session:
        # TODO: find a way to get all the tickets in support and print them to admin
        # i dunno if shit below works
        async with session.begin():
            tickets = await select(Ticket)
            for ticket in tickets:
                print(ticket)    
            return tickets        


async def add_user(telegram_id: int, username: str):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.telegram_id==telegram_id))

        existing_user = result.scalars().first()

        if existing_user is None:
            async with session.begin():
                user = User(telegram_id=telegram_id, username=username)
                session.add(user)
                session.commit()
        else:
            print("user already exists")


                  
async def get_users():
    async with async_session() as session:
        result = await session.scalar("select * from users")
        return result.fetchall()
    