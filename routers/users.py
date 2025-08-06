from fastapi import APIRouter, Body, Depends

from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from schema._input import UserInput, UpdateUserProfileInput, DeleteUserAccountInput
from db.engine import get_db
from operation.users import UsersOperation

router = APIRouter()

@router.post("/register")
async def register(
    db_session: Annotated[AsyncSession, 
    Depends(get_db)], data: UserInput = Body()
    ):
    user = await UsersOperation(db_session).create(
        username=data.username, 
        password=data.password
    )

    return user

@router.post("/login")
async def login(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: UserInput = Body()
):
    token = await UsersOperation(db_session).login(data.username, data.password)
    return token

@router.get("/{username}/")
async def get_user_profile(
    db_session: Annotated[AsyncSession,Depends(get_db)], username: str
    ):
    user_profile = await UsersOperation(db_session).get_user_by_username(username)

    return user_profile

@router.put("/")
async def upload_user_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: UpdateUserProfileInput = Body()
):
    user = await UsersOperation(db_session).update_username(
        data.old_username, data.new_username
        )
    
    return user

@router.delete("/{username}/")
async def delete_user_accouht(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: DeleteUserAccountInput = Body()
):
    await UsersOperation(db_session).user_delete_account(data.username)
