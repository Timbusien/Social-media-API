from database.models import User
from database import get_database
from datetime import datetime


# Регистрация
def register_user(name, surname, email, number, city, password):
    my_db = next(get_database())

    check = my_db.query(User).filter_by(email=email).first()

    if check:
        return 'Такой пользователь уже есть'

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
    else:
        return 'Ошибка данных'


# Добавить фото профиля
def add_profile_photo_my_db(user_id, profile_photo):
    my_db = next(get_database())

    check = my_db.query(User).filter_by(id=user_id).first()

    if check:
        check.profile_photo = profile_photo
        my_db.commit()
        return 'Фото профиля успешно добавлено'
    else:
        return False


# Изменить данные
def change_data_my_db(user_id, edit_data, new_data):
    my_db = next(get_database())
    exact_user = my_db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_data == 'name':
            exact_user.name = new_data
        elif edit_data == 'surname':
            exact_user.surname = new_data
        elif edit_data == 'email':
            exact_user.email = new_data
        elif edit_data == 'phone_number':
            exact_user.number = new_data
        elif edit_data == 'city':
            exact_user.city = new_data
        elif edit_data == 'password':
            exact_user.password = new_data

        my_db.commit()
        return 'Данные были успешно изменены'
    else:
        return 'Пользователь не найден'



# Удалить фото профиля
def delete_user_photo(user_id):
    my_db = next(get_database())

    check = my_db.query(User).filter_by(id=user_id).first()

    if check:
        check.profile_photo = 'None'
        my_db.commit()
        return 'Фото профиля было успешно удалено'
    else:
        return False


# Получение всех пользователей
def get_all_users():
    my_db = next(get_database())

    all_users = my_db.query(User).all()

    return all_users


# Получить информацию
def get_exact_user(user_id):
    my_db = next(get_database())

    user_info = my_db.query(User).filter_by(id=user_id).first()

    return user_info


# Удаление пользователя
def delete_user_my_db(user_id):
    my_db = next(get_database())
    delete_user = my_db.query(User).filter_by(user_id=user_id).first()

    if delete_user:
        my_db.delete(delete_user)
        my_db.commit()
        return 'Пользователь успешно удалён'
    else:
        return 'Пользователь не найден'


