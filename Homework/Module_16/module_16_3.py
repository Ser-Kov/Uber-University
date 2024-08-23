from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users():
    global users
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser')],
                      age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {int(current_index)} was registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                      username: str = Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1')) -> str:
    users.pop(str(user_id))
    return f'The user {user_id} has been deleted'
