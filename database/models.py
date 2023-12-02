from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    number = Column(String)
    city = Column(String)
    profile_photo = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


# Таблица для публикаций
class UserPost(Base):
    __tablename__ = 'user_posts'
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_text = Column(String)
    publish_data = Column(DateTime)
    user_fk = relationship(User, lazy='subquery')


# Таблица фоторафий
class Photo(Base):
    __tablename__ = 'post_photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('user_photos.id'))
    post_photo = Column(String)
    post_fk = relationship(UserPost, lazy='subquery')


# Таблица комментариев
class Comments(Base):
    __tablename__ = 'post_comments'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('users_posts.id'))
    comment_text = Column(String)
    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')






