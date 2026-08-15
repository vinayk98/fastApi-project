from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from router import articles
from db import models
from db.database import engine
#instance to represent the FastAPI application
app = FastAPI() 
app.include_router(blog_get.router) #include the router from blog_get.py
app.include_router(blog_post.router) #include the router from blog_post.py
app.include_router(user.router) #include the router from user.py
app.include_router(articles.router) #include the router from articles.py
models.Base.metadata.create_all(engine) #create the database tables based on the models defined in db/models.py