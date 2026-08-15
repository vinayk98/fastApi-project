from tkinter import Image
from typing import List, Optional
from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class BlogPost(BaseModel):
    title: str
    content: str
    published: bool = True
    comment_count: int = 0
    tags: Optional[List[str]] = []
    image_url: Optional[str] = None

@router.post("/new/{id}")
def create_blog(blog: BlogPost, id: int, version: int=1):
    """
    This API endpoint creates a new blog post with the provided title, content, publication status, and version.
    It also sets the response status code to 201 (Created) to indicate successful creation of the blog post.
    - **blog_title**: The title of the blog post.
    - **blog_content**: The content of the blog post.
    - **published**: Optional query parameter to indicate if the blog post is published (default is True).
    - **response**: The response object used to set the status code for the API response.
    """
    # response.status_code = status.HTTP_201_CREATED
    return {
        "id": id,
        "version": version,
        "data": blog
        }

@router.post("/new/{id}/comment")
def create_comment(blog: BlogPost,
 id: int, 
 comment_id: int= Query(None,
 title="Comment ID",
 description="The ID of the comment to be created for the blog post.",
 alias="commentId",
 deprecated=True),
 v: Optional[List[str]] = Query(["1", "2", "3"]),
 content: str = Body(Ellipsis, min_length=10, max_length=20, pattern="^[a-z\s]*$"),
 ):
    """
    This API endpoint creates a new comment for a specific blog post with the provided title, content, publication status, and version.
    It also sets the response status code to 201 (Created) to indicate successful creation of the comment.
    - **blog_title**: The title of the blog post.
    - **blog_content**: The content of the blog post.
    - **published**: Optional query parameter to indicate if the blog post is published (default is True).
    - **response**: The response object used to set the status code for the API response.
    """
    # response.status_code = status.HTTP_201_CREATED
    return {
        "blog_id": id,
        "comment_id": comment_id,
        "content": content,
        "data": blog,
        "version": v
        }
    
def required_functionality():
    return {"message": "fastapi is awesome!"}