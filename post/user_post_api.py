from fastapi import APIRouter, UploadFile, Body
from post import PublicPostModel, EditPostModel
from database.postservice import get_all_posts, get_exact_post, add_post,\
    add_post_photo, delete_post_db, edit_post

post_router = APIRouter(prefix='/user-post', tags=['Работа с публикациями'])


# Запрос на публикацию поста
@post_router.post('/public-post')
async def public_post(data: PublicPostModel):
    result = add_post(**data.model_dump())

    return {'meessage': result}


# Запрос на изменение поста
@post_router.put('/change-post')
async def change_post(data: EditPostModel):
    result = edit_post(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден'}


# Запрос на удаление поста
@post_router.delete('/delete-post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден'}


# Запрос на получение всех публикаций
@post_router.post('/get-all-posts')
async def all_posts():
    result = get_all_posts()

    return {'message': result}


# Добавление фотографий к посту
@post_router.post('/add_photo')
async def add_photo(post_id: int = Body(),
                    user_id: int = Body(),
                    photo_file: UploadFile = None):
    photo_path = f'/media/{photo_file.filename}'
    try:
        with open(f'media/{photo_file.filename}') as file:
            user_photo = await photo_file.read()

            file.write(user_photo)

        result = add_post_photo(post_id=post_id, post_photo=photo_path)

    except Exception as error:
        result = error

    return {'message': result}


# Получение определённого поста
@post_router.get('/get-exac-post')
async def get_exact(post_id: int):
    result = get_exact_post(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден'}














