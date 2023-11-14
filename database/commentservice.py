from database.models import Comments
# from datetime import datetime
from database import get_database


# Опубликовать комментарий
def add_comment(post_id, comment_text, user_id):
    my_db = next(get_database())

    new_comment = Comments(post_id=post_id, comment_text=comment_text, user_id=user_id)
    my_db.add(new_comment)
    my_db.commit()

    return 'Комментарий был успешно добавлен'


# Удаление комментария
def delete_comment(comment_id):
    my_db = next(get_database())

    delete = my_db.query(Comments).filter_by(id=comment_id).first()

    if delete:
        my_db.delete(delete_comment)
        my_db.commit()

        return 'Комментарий был успешно удалён'

    else:
        return False


# Изменить комментарий
def change_comment(comment_id, new_comment):
    my_db = next(get_database())

    change = my_db.query(Comments).filter_by(id=comment_id).first()

    if change:
        change.comment_text = new_comment
        my_db.commit()

        return 'Комментарий был успешно удалён'


# Получить все комментарии
def get_post_comment(post_id):
    my_db = next(get_database())

    post_comment = my_db.query(Comments).filter_by(post_id=post_id).first()

    return post_comment



