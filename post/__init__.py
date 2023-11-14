from pydantic import BaseModel

# Валидация поста
class PublicPostModel(BaseModel):
    user_id: int
    post_text: str


# Валидатор для изменения текста к посту
class EditPostModel(BaseModel):
    post_id: int
    new_text: str
    user_id: int

