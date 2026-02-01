from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.users import *

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

