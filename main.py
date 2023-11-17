from fastapi import FastAPI
from photo.photo_api import photo_router
from post.user_post_api import post_router
from comments.comment_api import comment_router
from database import Base, engine
from user.user_api import user_router

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')
app.include_router(photo_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(user_router)


@app.get('/test')
async def test():
    return 'This is test page'







