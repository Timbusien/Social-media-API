from pydantic import BaseModel

# Валидация публикации комментария
class CommentModel(BaseModel):
    comment_text: str
    user_id: int
    post_id: int


class EditCommentModel(BaseModel):
    new_text: str
    comment_id: int


