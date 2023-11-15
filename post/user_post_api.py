from fastapi import APIRouter, UploadFile
from post import PublicPostModel, EditPostModel
from database.postservice import get_all_posts, get_exact_post, add_post,\
    edit_post, delete_post_db, edit_post_db

post_router = APIRouter(prefix='/user-post', tags=['Работа с публикациями'])


# Запрос на публикацию поста
@post_router.post('/public-post')
async def public_post(data: PublicPostModel):
    result = add_post(**data.model_dump())

    return {'meessage': result}


# Запрос на изменение поста
@post_router.put('/change-post')
async def change_post(data: EditPostModel):
    result = edit_post_db(**data.model_dump())

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





