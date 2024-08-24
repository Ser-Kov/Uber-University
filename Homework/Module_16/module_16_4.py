from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List


app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser')],
                      age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> User:
    new_user = User(id=len(users) + 1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                      username: str = Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> User:
    for user in users:
        if user_id == user.id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1')) -> User:
    for user in users:
        if user_id == user.id:
            users.pop(users.index(user))
            return user
    raise HTTPException(status_code=404, detail='User was not found')

