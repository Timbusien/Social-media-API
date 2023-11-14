from fastapi import APIRouter, UploadFile

photo_router = APIRouter(prefix='/photo', tags=['Фотографии'])


# Добавление фото
@photo_router.post('/add-photo')
async def add_users_photo(photo_file: UploadFile, user_id: int):
    print(photo_file.filename)
    # Сохранение фотографии
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()
        file.write(user_photo)

    return {'message': 'Successfully'}


# Изменение фотографии
@photo_router.put('/edit-photo')
async def edit_users_photo(new_photo_file: UploadFile, user_id: int):
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()
        file.write(user_photo)

    return {'message': 'Successfully changed'}


# Удаление фотографии
@photo_router.delete('/delete-photo')
async def delete_users_photo(user_id: int):
    pass





