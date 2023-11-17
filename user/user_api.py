from fastapi import APIRouter
from user import LoginProfileModel, RegisterUserValidator, EditUserValidator
from database.userservice import register_user, login_user, add_profile_photo_my_db, change_data, delete_user_photo, get_all_users, get_exact_user

user_router = APIRouter(prefix='/user', tags=['Управление пользователями'])


# Вход в аккаунт
@user_router.post('/login')
async def login(data: LoginProfileModel):
    result = login_user(**data.model_dump())

    return {'message': result}


# Регистрация
@user_router.post('/register')
async def register(data: RegisterUserValidator):
    result = register_user(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь уже есть'}


# Запрос на получение информации о пользователе
@user_router.get('/get-user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users()
        return {'message': result}
    else:
        result = get_exact_user(user_id)
        return {'message': result}



