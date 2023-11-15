from fastapi import APIRouter
from user import UserProfileModel
from database.userservice import register_user, login_user, add_profile_photo_my_db, change_data, delete_user_photo, get_all_users, get_info_user


