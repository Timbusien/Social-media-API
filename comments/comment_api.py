from fastapi import APIRouter
from comments import CommentModel, EditCommentModel
from database.commentservice import change_comment, add_comment, delete_comment_db, get_post_comment

comment_router = APIRouter(prefix='/comment', tags=['Комментарии'])


# Запрос на публикацию комментария -> add_comment
@comment_router.post('/public-comment')
async def new_comment(data: CommentModel):
    result = add_comment(**data.model_dump())

    return {'message': result}


# Запрос на изменение комментария -> edit_comment
@comment_router.put('/change-comment')
async def edit_comment(data: EditCommentModel):
    result = change_comment(**data.model_dump())

    if result:
        return {'message': result}

    else:
        return {'message': 'Комментарий не найден'}


# Запрос на удаление комментариев -> delete_comment
@comment_router.delete('/delete-comment')
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)

    if result:
        return {'message': result}
    else:
        return {'message': result}


# Запрос на получение комментариев к определённым публикациям -> get_comments
@comment_router.get('/get-comment')
async def get_comment(post_id: int):
    result = get_post_comment(post_id)

    return {'message': result}



