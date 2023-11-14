from fastapi import APIRouter
from comments import CommentModel, EditCommentModel
from database.commentservice import change_comment, add_comment, delete_comment, get_post_comment

comment_router = APIRouter(prefix='/comment', tags=['Комментарии'])

# Запрос на публикацию комментария -> add_comment
# Запрос на изменение комментария -> edit_comment
# Запрос на удаление комментариев -> delete_comment
# Запрос на получение комментариев к определённым публикациям -> get_comments
