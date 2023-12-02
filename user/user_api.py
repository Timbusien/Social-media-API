import os
from pathlib import Path
from fastapi import APIRouter, UploadFile, HTTPException
from user import LoginProfileModel, RegisterUserValidator, EditUserValidator
from database.userservice import register_user, login_user, delete_user_my_db, add_profile_photo_my_db, change_data_my_db, delete_user_photo, get_all_users, get_exact_user


user_router = APIRouter(prefix='/user', tags=['Управление пользователями'])

upload_folder = ''

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


@user_router.put('/change-data')
async def change(data: EditUserValidator):
    change_data = data.model_dump()
    result = change_data_my_db(**change_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь не найден'}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_my_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь не найден'}


@user_router.post('/add-avatar')
async def add_user_profile_photo(photo_file: UploadFile):
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)

    return {'message': 'Success'}


@user_router.put('/edit-avatar')
async def edit_user_avatar(new_photo_file: UploadFile):
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()
        file.write(user_photo)

    return {'message': 'Successfully changed'}


@user_router.delete('/delete-avatar')
async def delete_user_avatar(filename: str):
    file_path = os.path.join(upload_folder, filename)

    if not Path(file_path).is_file():
        raise HTTPException(status_code=404, detail='File not found')
    os.remove(file_path)

    return {'message': 'Deleted successfully'}
