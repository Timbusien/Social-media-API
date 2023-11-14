from database.models import User
from database import get_database
from datetime import datetime


# Регистрация
def register_user(name, surname, email, number, city, password):
    my_db = next(get_database())

    check = my_db.query(User).filter_by(email=email).first()

    if check:
        return True

    new_user = User(name=name,
                    surname=surname,
                    number=number,
                    city=city,
                    password=password,
                    reg_date=datetime.now())
    my_db.add(new_user)
    my_db.commit()

    return 'Пользователь успешно зарегистрирован'


# Вход в аккаунт
def login_user(email, password):
    my_db = next(get_database())

    check = my_db.query(User).filter_by(email=email).first()

    if check:
        if check.password == password:
            return check
        elif check.password != password:
            return 'Неверный пароль'
    return 'Ошибка данных'


# Добавить фото профиля
def add_profile_photo_my_db(user_id, profile_photo):
    my_db = next(get_database())

    check = my_db.query(User).filter_by(id=user_id).first()

    if check:
        check.profile_photo = profile_photo
        my_db.commit()

        return 'Фото профиля успешно добавлено'

    return False


# Изменить данные
def change_data(name, surname, number, city, password):
    my_db = next(get_database())

    change_user = User(name=name,
                    surname=surname,
                    number=number,
                    city=city,
                    password=password,
                    reg_date=datetime.now())
    my_db.add(change_user)
    my_db.commit()

    return 'Информация была успешно изменена'


# Удалить фото профиля
def delete_user_photo(user_id):
    my_db = next(get_database())

    check = my_db.query(User).filter_by(id=user_id).first()

    if check:
        check.profile_photo = 'None'
        my_db.commit()

        return 'Фото профиля было успешно удалено'

    return False


# Получение всех пользователей
def get_all_users():
    my_db = next(get_database())

    all_users = my_db.query(User).all()

    return all_users


# Получить информацию
def get_info_user(user_id):
    my_db = next(get_database())

    user_info = my_db.query(User).filter_by(id=user_id).first()

    return user_info


