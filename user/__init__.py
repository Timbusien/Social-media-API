from pydantic import BaseModel


# Валидатор для входа в аккаунт
class LoginProfileModel(BaseModel):
    email: str
    password: str


# Валидатор для регистрации
class RegisterUserValidator(BaseModel):
    name: str
    surname: str
    email: str
    number:str
    city: str
    password: str


# Валидатор для изменения данных пользователя
class EditUserValidator(BaseModel):
    user_id: int
    edit_data: str
    new_data: str


