from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..domain.users import *
from ..domain.subscriptions import *
from ..domain.configs import *

async def create_new_user(session: AsyncSession, username: str, invited_by: int, 
                          can_take_test: bool, rank: str):
    new_user = User(username=username, invited_by=invited_by, can_take_test=can_take_test, rank=rank)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def delete_user(session: AsyncSession, name: str): # name is username in table
    " delete by username because username is unquie value"

    curr_user = select(User).where(User.username == name)
    db_object = await session.scalars(curr_user).one()

    if not db_object:
        return False
    else:
        await session.delete(db_object)
        await session.commit()
        return True
    
async def change_user(*args):
    pass


async def get_user_by_id(session: AsyncSession, id: int):
    return await session.scalar(
        select(User).where(User.user_id == id)
    )

async def get_user_by_id_username(session: AsyncSession, name: int):
    return await session.scalar(
        select(User).where(User.username == name)
    )

async def get_user_by_id_subscription(session: AsyncSession, sub_id: int):
    result = await session.execute(select(User, Subscriptions)
        .join(Subscriptions, User.user_id == Subscriptions.user_id )
        .where(Subscriptions.id == sub_id))
    return result.scalar_one_or_none()

async def get_user_by_id_config(session: AsyncSession, conf_id: int):
    result = await session.execite(select(User, Configs)
        .join(Configs, User.user_id == Configs.user_id)
        .where(Configs.id == conf_id))
    return result.scalar_one_or_none()


    
