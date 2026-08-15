from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exceptions import StoryException
from router import blog_get, blog_post, user, product, articles
from auth import authentication
from db import models
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine


#instance to represent the FastAPI application
app = FastAPI() 
app.include_router(blog_get.router) #include the router from blog_get.py
app.include_router(blog_post.router) #include the router from blog_post.py
app.include_router(user.router) #include the router from user.py
app.include_router(product.router) #include the router from product.py
app.include_router(articles.router) #include the router from articles.py
app.include_router(authentication.router)

#used for custom exception handling in FastAPI. It allows you to define a function that will be called whenever a specific exception is raised in your application.
@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a teapot."},
    )


models.Base.metadata.create_all(engine) #create the database tables based on the models defined in db/models.py
origins = ["http://localhost:3000"] #define the allowed origins for CORS (Cross-Origin Resource Sharing) requests
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]) #add CORS middleware to the application