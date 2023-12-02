from database.models import UserPost, Photo
from datetime import datetime
from database import get_database


# Разместить пост
def add_post(user_id, post_text):
    my_db = next(get_database())

    new_post = UserPost(user_id=user_id, post_text=post_text, publish_data=datetime.now())

    my_db.add(new_post)
    my_db.commit()

    return 'Пост был успешно добавлен'


# Добавить фото для поста
def add_post_photo(post_id, post_photo):
    my_db = next(get_database())

    new_post = Photo(post_id=post_id, post_photo=post_photo)

    my_db.add(new_post)
    my_db.commit()

    return 'Фотография была успешно добавлена'


# Удалить пост
def delete_post_db(user_id):
    my_db = next(get_database())

    check_post = my_db.query(UserPost).filter_by(user_id=user_id).first()
    post_photos = my_db.query(Photo).filter_by(user_id=user_id).first()

    if check_post:
        my_db.delete(check_post)
        my_db.commit()
        my_db.delete(post_photos)
        my_db.commit()

    return 'Пост был успешно удалён'


# Получить все посты
def get_all_posts():
    my_db = next(get_database())

    all_posts = my_db.query(UserPost).all()

    return all_posts


# Получить определённый пост
def get_exact_post(user_id):
    my_db = next(get_database())
    exact_post = my_db.query(UserPost).filter_by(id=user_id).first()

    if exact_post:
        return exact_post
    else:
        return False


def edit_post(post_id, user_id, new_text):
    my_db = next(get_database())

    exact_post = my_db.query(UserPost).filter_by(post_id=post_id, user_id=user_id).first()

    if exact_post:
        exact_post.post_text = new_text
        my_db.commit()

        return 'Успешно изменено'

    return False

